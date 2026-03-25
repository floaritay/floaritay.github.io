# 我要做一个图像分割的简单实现。
# 树上芒果实例分割数据集(data18) ：
# 为树上芒果检测和分割而创建的数据集。使用带有多边形区域注释的VGG图像注释工具（Dutta & Zisserman 2019）对图像进行注释。两个文件夹包含用于训练和文本图像集的 COCO 注释格式的图像和 JSON 注释文件。数据集描述如下：
# 文件夹 1 - 平铺图像 - 总计 542 张（训练 + 测试） 640 x 540 像素的平铺图像 
# 文件夹 2 - 单个芒果剪 - 总计 1200 个（训练 + 测试） 剪
# 训练集与测试集文件地址如下：
# 文件夹2（测试集）：/data/shixunfiles/3a2b8256a18499c8b84a46b04cc63d8c_1705368625397.zip
# 文件夹1（测试集）：/data/shixunfiles/58071852bccf513d21f51e4c4b28053b_1705368623909.zip
# 文件夹2（训练集）：/data/shixunfiles/3098a61bfaed1f5870d879e447a09e64_1705279814011.zip
# 文件夹1（训练集）：/data/shixunfiles/f38d473718e2aefcd940898e643fd0cd_1704251553388.zip
# 把他们解压到：
# /data/workspace/downloadfiles
# 完成相应的代码
# 代码要完成
# 1.读取数据
# 2.预处理：数据划分（训练和预测）
# 3.定义模型： 只允许调现有机器学习库模型，不使用深度网络
# 4.训练模型
# 5.模型预测与评估（自测）： 输出预测结果； 预测结果评价； 最优模型保存（my_model.joblib）

# 现已经完成了解压，包含四个文件夹：data18_train，data18_test，data18_train2，data18_test2。里面都是png格式的图片，每个文件夹各有一个json注释文件。

# 请你给出代码，每个步骤开始要有注释说明这是哪一步
# 另外我是在一个云平台的jupyter中完成的，每一步都是一个cell，而且云平台环境有限，不要使用复杂的模型，不要内存太大等

# 1. 导入必要的库
import os
import json
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from skimage import feature, segmentation, morphology
from sklearn.metrics import accuracy_score, jaccard_score
import joblib
from tqdm import tqdm
import matplotlib.pyplot as plt

# 2. 读取数据：从 data18_train 文件夹加载图像和 COCO 格式注释

# 设置数据根路径（Windows 路径）
DATA_ROOT = r"D:\DownloadFiles\downloadfiles1"
TRAIN_FOLDER = "data18_train2"
folder_path = os.path.join(DATA_ROOT, TRAIN_FOLDER)

# 查找 JSON 注释文件（假设只有一个 .json 文件）
json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
if not json_files:
    raise FileNotFoundError("未找到 JSON 注释文件！")
annotation_file = os.path.join(folder_path, json_files[0])

# 加载 COCO 格式注释
with open(annotation_file, 'r', encoding='utf-8') as f:
    coco_data = json.load(f)

# 构建图像 ID 到文件名的映射
id_to_filename = {img['id']: img['file_name'] for img in coco_data['images']}
annotations = coco_data['annotations']

print(f"成功加载注释文件: {os.path.basename(annotation_file)}")
print(f"图像数量: {len(coco_data['images'])}, 标注实例数: {len(annotations)}")

# 3. 预处理：提取每张图像的像素特征 + 构建二值分割标签（芒果 vs 背景）
#    并将所有数据合并后划分为训练集和验证集（按像素）

def extract_pixel_features(image):
    """
    为每个像素提取轻量级手工特征（共4维）：
      - R, G, B 通道（归一化到 [0,1]）
      - 梯度幅值（Sobel 边缘强度，归一化）
    返回形状: (H*W, 4)
    """
    # 归一化 RGB
    img_norm = image.astype(np.float32) / 255.0
    r = img_norm[:, :, 0].flatten()
    g = img_norm[:, :, 1].flatten()
    b = img_norm[:, :, 2].flatten()

    # 计算梯度幅值（边缘特征）
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    grad_x = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
    magnitude = np.sqrt(grad_x**2 + grad_y**2)
    grad_mag = (magnitude / 255.0).flatten()  # 归一化

    features = np.stack([r, g, b, grad_mag], axis=1)  # (H*W, 4)
    return features

def create_binary_mask(img_shape, ann_list):
    """
    根据该图像的所有多边形注释，生成一个二值掩码（1=芒果，0=背景）
    img_shape: (H, W, C)
    ann_list: 该图像对应的所有 annotation 字典列表
    """
    mask = np.zeros(img_shape[:2], dtype=np.uint8)
    for ann in ann_list:
        # COCO 多边形格式: [x1,y1,x2,y2,...]
        poly = np.array(ann['segmentation'][0]).reshape(-1, 2).astype(np.int32)
        cv2.fillPoly(mask, [poly], 1)
    return mask

# ----------------------------
# 限制图像数量以节省内存
MAX_IMAGES = 80  # 可根据云平台内存调整（建议 50~100）

# 获取所有训练图像 ID（最多取 MAX_IMAGES 张）
all_image_ids = list(id_to_filename.keys())
selected_ids = all_image_ids[:MAX_IMAGES]

X_all = []  # 特征列表
y_all = []  # 标签列表

print("正在提取特征和标签...")
for img_id in tqdm(selected_ids):
    filename = id_to_filename[img_id]
    img_path = os.path.join(folder_path, filename)
    
    if not os.path.exists(img_path):
        print(f"警告：图像不存在 {img_path}")
        continue
        
    # 读取图像
    image = cv2.imread(img_path)
    if image is None:
        continue
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 获取该图像的所有标注
    img_anns = [ann for ann in annotations if ann['image_id'] == img_id]
    if not img_anns:
        continue  # 跳过无标注图像
    
    # 构建二值掩码
    mask = create_binary_mask(image.shape, img_anns)
    
    # 提取特征和标签（展平）
    X = extract_pixel_features(image)   # (H*W, 4)
    y = mask.flatten()                  # (H*W,)
    
    X_all.append(X)
    y_all.append(y)

# 合并所有图像的数据
X_combined = np.vstack(X_all)  # (N_pixels, 4)
y_combined = np.hstack(y_all)  # (N_pixels,)

print(f"总像素样本数: {X_combined.shape[0]}")

# 划分训练集和验证集（按像素，保持类别比例）
X_train, X_val, y_train, y_val = train_test_split(
    X_combined, y_combined,
    test_size=0.2,
    random_state=42,
    stratify=y_combined  # 保证正负样本比例一致
)

print(f"训练集像素数: {X_train.shape[0]}, 验证集像素数: {X_val.shape[0]}")
print(f"芒果像素占比（训练）: {y_train.mean():.4f}")

# 4. 定义并训练模型：使用轻量级 Random Forest（非深度学习）
#    限制树的数量和深度，避免内存爆炸

print("正在初始化模型...")
model = RandomForestClassifier(
    n_estimators=25,      # 树的数量（不宜过大）
    max_depth=12,         # 最大深度
    min_samples_split=20, # 内部节点再划分所需最小样本数
    random_state=42,
    n_jobs=-1             # 使用所有 CPU 核心加速
)

print("开始训练模型（可能需要几分钟）...")
model.fit(X_train, y_train)
print("✅ 模型训练完成！")

# 5. 模型预测、评估、可视化结果，并保存模型
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
# 在验证集上预测
print("正在预测验证集...")
y_pred_val = model.predict(X_val)

# 评估指标
acc = accuracy_score(y_val, y_pred_val)
iou = jaccard_score(y_val, y_pred_val, pos_label=1)  # 芒果类的 IoU

print(f"\n📊 评估结果（验证集）:")
print(f"  - 像素准确率: {acc:.4f}")
print(f"  - 芒果区域 IoU: {iou:.4f}")

# 保存模型
joblib.dump(model, 'my_model.joblib')
print("\n💾 模型已保存为: my_model.joblib")

# ----------------------------
# 可视化一个预测示例（从训练集中选第一张有效图像）
sample_id = selected_ids[0]
filename = id_to_filename[sample_id]
img_path = os.path.join(folder_path, filename)

image = cv2.imread(img_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 获取真实掩码
sample_anns = [ann for ann in annotations if ann['image_id'] == sample_id]
gt_mask = create_binary_mask(image.shape, sample_anns)

# 预测整图
X_full = extract_pixel_features(image)
pred_flat = model.predict(X_full)
pred_mask = pred_flat.reshape(image.shape[:2])

# 显示对比图
plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
plt.title("原始图像")
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("真实掩码（Ground Truth）")
plt.imshow(gt_mask, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title(f"预测掩码 (IoU≈{iou:.3f})")
plt.imshow(pred_mask, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()


# 6. 加载保存的模型，对 data18_test 测试集进行预测与评估

import os
import json
import numpy as np
import cv2
import joblib
from tqdm import tqdm
from sklearn.metrics import accuracy_score, jaccard_score
import matplotlib.pyplot as plt

# ----------------------------
# 配置路径
DATA_ROOT = r"D:\DownloadFiles\downloadfiles1"
TEST_FOLDER = "data18_test2"
test_folder_path = os.path.join(DATA_ROOT, TEST_FOLDER)

# 查找测试集 JSON 注释文件
json_files = [f for f in os.listdir(test_folder_path) if f.endswith('.json')]
if not json_files:
    raise FileNotFoundError("未在测试文件夹中找到 JSON 注释文件！")
test_annotation_file = os.path.join(test_folder_path, json_files[0])

# 加载测试集注释
with open(test_annotation_file, 'r', encoding='utf-8') as f:
    test_coco = json.load(f)

id_to_filename_test = {img['id']: img['file_name'] for img in test_coco['images']}
test_annotations = test_coco['annotations']

print(f"加载测试集: {len(id_to_filename_test)} 张图像，{len(test_annotations)} 个标注实例")

# ----------------------------
# 加载训练好的模型
model = joblib.load('my_model.joblib')
print("✅ 模型加载成功！")

# ----------------------------
# 复用之前的特征提取和掩码生成函数（保持一致！）
def extract_pixel_features(image):
    img_norm = image.astype(np.float32) / 255.0
    r = img_norm[:, :, 0].flatten()
    g = img_norm[:, :, 1].flatten()
    b = img_norm[:, :, 2].flatten()
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    grad_x = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
    magnitude = np.sqrt(grad_x**2 + grad_y**2)
    grad_mag = (magnitude / 255.0).flatten()
    return np.stack([r, g, b, grad_mag], axis=1)

def create_binary_mask(img_shape, ann_list):
    mask = np.zeros(img_shape[:2], dtype=np.uint8)
    for ann in ann_list:
        poly = np.array(ann['segmentation'][0]).reshape(-1, 2).astype(np.int32)
        cv2.fillPoly(mask, [poly], 1)
    return mask

# ----------------------------
# 在测试集上逐图预测并收集所有像素的真实标签和预测标签
all_y_true = []
all_y_pred = []

# 可选：限制测试图像数量以加速（例如只测前 30 张）
MAX_TEST_IMAGES = 50
test_image_ids = list(id_to_filename_test.keys())[:MAX_TEST_IMAGES]

print(f"正在对 {len(test_image_ids)} 张测试图像进行预测...")
for img_id in tqdm(test_image_ids):
    filename = id_to_filename_test[img_id]
    img_path = os.path.join(test_folder_path, filename)
    
    if not os.path.exists(img_path):
        continue
        
    image = cv2.imread(img_path)
    if image is None:
        continue
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 获取真实标注
    img_anns = [ann for ann in test_annotations if ann['image_id'] == img_id]
    if not img_anns:
        # 若无标注，跳过（或可视为全背景）
        continue
        
    gt_mask = create_binary_mask(image.shape, img_anns)
    y_true = gt_mask.flatten()
    
    # 预测
    X_test_img = extract_pixel_features(image)
    y_pred = model.predict(X_test_img)
    
    all_y_true.append(y_true)
    all_y_pred.append(y_pred)

# 合并所有测试像素
y_true_all = np.hstack(all_y_true)
y_pred_all = np.hstack(all_y_pred)

# ----------------------------
# 计算整体评估指标
test_acc = accuracy_score(y_true_all, y_pred_all)
test_iou = jaccard_score(y_true_all, y_pred_all, pos_label=1)

print("\n📊 测试集最终评估结果:")
print(f"  - 像素准确率 (Accuracy): {test_acc:.4f}")
print(f"  - 芒果区域 IoU:          {test_iou:.4f}")

# ----------------------------
# 可视化部分测试结果（展示前3张）
num_show = min(3, len(test_image_ids))
plt.figure(figsize=(15, 4 * num_show))

for idx, img_id in enumerate(test_image_ids[:num_show]):
    filename = id_to_filename_test[img_id]
    img_path = os.path.join(test_folder_path, filename)
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 真实掩码
    img_anns = [ann for ann in test_annotations if ann['image_id'] == img_id]
    gt_mask = create_binary_mask(image.shape, img_anns)
    
    # 预测掩码
    X_full = extract_pixel_features(image)
    pred_flat = model.predict(X_full)
    pred_mask = pred_flat.reshape(image.shape[:2])
    
    # 绘图
    plt.subplot(num_show, 3, idx * 3 + 1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis('off')
    
    plt.subplot(num_show, 3, idx * 3 + 2)
    plt.imshow(gt_mask, cmap='gray')
    plt.title("Ground Truth")
    plt.axis('off')
    
    plt.subplot(num_show, 3, idx * 3 + 3)
    plt.imshow(pred_mask, cmap='gray')
    plt.title(f"Prediction (IoU≈{test_iou:.3f})")
    plt.axis('off')

plt.tight_layout()
plt.show()

# 7. 对测试集预测结果进行后处理，并可视化对比效果

import cv2
import numpy as np
from tqdm import tqdm
from sklearn.metrics import accuracy_score, jaccard_score
import matplotlib.pyplot as plt

def postprocess_mask(pred_mask, min_area=200):
    """
    对二值预测掩码进行后处理：
      - 开运算：去除小噪点
      - 闭运算：填充内部小孔洞
      - 连通区域分析：移除面积小于 min_area 的区域
    输入: pred_mask (H, W), 值为 0 或 1 (int/bool)
    输出: processed_mask (H, W), 值为 0 或 1
    """
    # 转为 OpenCV 所需的 uint8 格式（0 或 255）
    mask_uint8 = (pred_mask * 255).astype(np.uint8)
    
    # 1. 开运算（去噪）
    kernel_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask_open = cv2.morphologyEx(mask_uint8, cv2.MORPH_OPEN, kernel_open)
    
    # 2. 闭运算（填洞）
    kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask_closed = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel_close)
    
    # 3. 连通区域过滤
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
        mask_closed, connectivity=8
    )
    output_mask = np.zeros_like(mask_closed)
    for i in range(1, num_labels):  # label 0 是背景
        if stats[i, cv2.CC_STAT_AREA] >= min_area:
            output_mask[labels == i] = 255
    
    # 转回 0/1 格式
    return (output_mask // 255).astype(np.uint8)

# ----------------------------
# 使用之前已加载的变量（避免重复读图）：
#   - test_image_ids
#   - id_to_filename_test
#   - test_folder_path
#   - test_annotations
#   - model

# 收集后处理后的预测结果
all_y_true_pp = []
all_y_pred_pp = []

print("正在对测试集预测结果进行后处理...")
for img_id in tqdm(test_image_ids):
    filename = id_to_filename_test[img_id]
    img_path = os.path.join(test_folder_path, filename)
    if not os.path.exists(img_path):
        continue
        
    image = cv2.imread(img_path)
    if image is None:
        continue
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 真实标签
    img_anns = [ann for ann in test_annotations if ann['image_id'] == img_id]
    if not img_anns:
        continue
    gt_mask = create_binary_mask(image.shape, img_anns)
    y_true = gt_mask.flatten()
    
    # 原始预测（和之前一样）
    X_test_img = extract_pixel_features(image)
    y_pred_raw = model.predict(X_test_img)
    pred_mask_raw = y_pred_raw.reshape(image.shape[:2])
    
    # 后处理
    pred_mask_pp = postprocess_mask(pred_mask_raw, min_area=200)
    y_pred_pp = pred_mask_pp.flatten()
    
    all_y_true_pp.append(y_true)
    all_y_pred_pp.append(y_pred_pp)

# 合并所有像素
y_true_all_pp = np.hstack(all_y_true_pp)
y_pred_all_pp = np.hstack(all_y_pred_pp)

# 评估后处理性能
test_acc_pp = accuracy_score(y_true_all_pp, y_pred_all_pp)
test_iou_pp = jaccard_score(y_true_all_pp, y_pred_all_pp, pos_label=1)

print("\n📊 后处理效果对比:")
print(f"原始预测   -> Acc: {test_acc:.4f}, IoU: {test_iou:.4f}")
print(f"后处理后   -> Acc: {test_acc_pp:.4f}, IoU: {test_iou_pp:.4f}")

# ----------------------------
# 可视化对比：选第一张测试图像
sample_id = test_image_ids[0]
filename = id_to_filename_test[sample_id]
img_path = os.path.join(test_folder_path, filename)

image = cv2.imread(img_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 真实掩码
img_anns = [ann for ann in test_annotations if ann['image_id'] == sample_id]
gt_mask = create_binary_mask(image.shape, img_anns)

# 原始预测
X_full = extract_pixel_features(image)
pred_raw_flat = model.predict(X_full)
pred_mask_raw = pred_raw_flat.reshape(image.shape[:2])

# 后处理预测
pred_mask_pp = postprocess_mask(pred_mask_raw, min_area=200)

# 绘图：4列对比
plt.figure(figsize=(16, 4))

plt.subplot(1, 4, 1)
plt.title("原始图像")
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 4, 2)
plt.title("真实掩码")
plt.imshow(gt_mask, cmap='gray')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.title("原始预测")
plt.imshow(pred_mask_raw, cmap='gray')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.title(f"后处理结果\n(IoU={test_iou_pp:.3f})")
plt.imshow(pred_mask_pp, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()