# 数据集（作物图像）包含每种农业作物（玉米、小麦、黄麻、水稻和甘蔗）的40多张图像。
# "D:\DownloadFiles\downloadfiles"下的五个文件夹'jute', 'maize', 'rice', 'sugarcane', 'wheat'，都为jpeg格式
# ==================================================
# 1. 读取数据：加载所有图像和对应类别标签
# ==================================================
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
from scipy import ndimage
import matplotlib.pyplot as plt
import seaborn as sns

# 数据根目录（已解压）
data_dir = r"D:\DownloadFiles\downloadfiles"
categories = ['jute', 'maize', 'rice', 'sugarcane', 'wheat']

# 统一图像尺寸（越小越快，64x64 平衡速度与信息）
IMG_SIZE = (64, 64)

images = []
labels = []

print("正在读取图像...")

# 遍历每个类别文件夹
for category in categories:
    folder = os.path.join(data_dir, category)
    for img_file in os.listdir(folder):
        path = os.path.join(folder, img_file)
        # 读取图像
        img = cv2.imread(path)
        if img is None:
            continue  # 跳过无效图像
        # 缩放图像
        img = cv2.resize(img, IMG_SIZE)
        # 转为 RGB（可选，但保持一致性）
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        images.append(img)
        labels.append(category)

print(f"共读取 {len(images)} 张图像。")

# ==================================================
# 2. 预处理：划分训练集和测试集 + 特征展平 + 标签编码
# ==================================================
# 图像增强函数
def augment_image(image):
    """对单张图像进行多种增强操作"""
    augmented_images = [image]  # 原始图像
    
    # 随机水平翻转
    flipped_h = np.fliplr(image)
    augmented_images.append(flipped_h)
    
    # 亮度调整 - 使用固定值而不是随机值
    brightness_factors = [0.7, 1.3]  # 固定的亮度调整因子
    for factor in brightness_factors:
        bright_adjusted = np.clip(image * factor, 0, 255).astype(np.uint8)
        augmented_images.append(bright_adjusted)
    
    return augmented_images

# 对每张图像进行增强
augmented_images = []
augmented_labels = []

for img, label in zip(images, labels):
    augmented_batch = augment_image(img)
    augmented_images.extend(augmented_batch)
    augmented_labels.extend([label] * len(augmented_batch))

# 转换为numpy数组
images = np.array(augmented_images)
labels = np.array(augmented_labels)

print(f"数据增强后，共有 {len(images)} 张图像。")

print('部分增强后的图像如下：')
# 随机展示六张增强后的图片
def show_random_images(images, labels, n=6):
    """从图像列表中随机选取n个，并显示"""
    indices = np.random.choice(len(images), size=n, replace=False)
    selected_images = images[indices]
    selected_labels = labels[indices]

    plt.figure(figsize=(10, 10))
    for i, (img, label) in enumerate(zip(selected_images, selected_labels)):
        plt.subplot(2, 3, i + 1)
        plt.imshow(img)
        plt.title(label)
        plt.axis('off')
    plt.show()

# 展示随机的六张增强后的图片
show_random_images(images, labels)

# 将字符串标签转为数字（0~4）
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)  # 使用之前训练的编码器对新标签进行编码

# 展平图像：(N, 64, 64, 3) → (N, 12288)
X = images.reshape(images.shape[0], -1)

# 划分训练集（80%）和测试集（20%），保持各类别比例
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

print(f"训练集: {X_train.shape[0]} 张，测试集: {X_test.shape[0]} 张")

# ==================================================
# 3. 定义模型：手动标准化 + SVM
# ==================================================

# 步骤1：对训练特征进行标准化（均值0，方差1）
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# 步骤2：创建 SVM 模型（最基础配置）
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)


# ==================================================
# 4. 训练模型
# ==================================================
svm_model.fit(X_train_scaled, y_train)

print("SVM 模型训练完成。")

# ==================================================
# 5. 模型预测与评估：输出结果、评价指标、保存模型
# ==================================================

# 对测试集做同样的标准化（注意：用训练集的 scaler！）
X_test_scaled = scaler.transform(X_test)

# 进行预测
y_pred = svm_model.predict(X_test_scaled)

# 计算准确率
acc = accuracy_score(y_test, y_pred)
print(f"\n>>> 测试准确率: {acc:.4f} ({acc*100:.2f}%)")

# 打印每个类别的详细评估
print("\n=== 分类报告 ===")
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)
print(report)

# 绘制混淆矩阵
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

print("\n✅ 公测评估完成！")

# # 保存模型和标准化器（两者都需要，否则无法预测新图）
# # joblib.dump(svm_model, 'my_model.joblib')
# # joblib.dump(scaler, 'scaler.joblib')          # 必须保存！用于新数据标准化
# # joblib.dump(label_encoder, 'label_encoder.joblib')

# # print("\n✅ 模型、标准化器、标签编码器均已保存。")


# # 导入所需库
# import os
# import cv2
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# import matplotlib.pyplot as plt
# import seaborn as sns
# from skimage.feature import hog

# # 设置数据路径和类别
# data_dir = r"D:\DownloadFiles\downloadfiles"
# categories = ['jute', 'maize', 'rice', 'sugarcane', 'wheat']
# IMG_SIZE = (128, 128)

# # 读取图像
# images = []
# labels = []

# print("正在读取图像...")
# for category in categories:
#     folder = os.path.join(data_dir, category)
#     for img_file in os.listdir(folder):
#         path = os.path.join(folder, img_file)
#         img = cv2.imread(path)
#         if img is None:
#             continue
#         img = cv2.resize(img, IMG_SIZE)
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         images.append(img)
#         labels.append(category)

# images = np.array(images)
# labels = np.array(labels)
# print(f"共读取 {len(images)} 张图像。")

# # 提取 HOG + HSV 特征
# def extract_combined_features(images, img_size=(128, 128)):
#     hog_features = []
#     color_features = []
    
#     for img in images:
#         resized = cv2.resize(img, img_size)
        
#         # HOG 特征
#         gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
#         hog_feat = hog(
#             gray,
#             orientations=9,
#             pixels_per_cell=(16, 16),
#             cells_per_block=(2, 2),
#             block_norm='L2-Hys',
#             transform_sqrt=True,
#             feature_vector=True
#         )
        
#         # HSV 颜色直方图
#         hsv = cv2.cvtColor(resized, cv2.COLOR_RGB2HSV)
#         hist_h = cv2.calcHist([hsv], [0], None, [50], [0, 180])
#         hist_s = cv2.calcHist([hsv], [1], None, [60], [0, 256])
#         hist_v = cv2.calcHist([hsv], [2], None, [60], [0, 256])
#         color_hist = np.concatenate([hist_h.flatten(), hist_s.flatten(), hist_v.flatten()])
        
#         hog_features.append(hog_feat)
#         color_features.append(color_hist)
    
#     hog_features = np.array(hog_features)
#     color_features = np.array(color_features)
#     combined = np.hstack([hog_features, color_features])
    
#     return combined

# print("正在提取 HOG + HSV 组合特征...")
# X = extract_combined_features(images, img_size=IMG_SIZE)

# # 标签编码
# label_encoder = LabelEncoder()
# y = label_encoder.fit_transform(labels)

# # 划分训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, stratify=y, random_state=42
# )

# # 标准化
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# # 训练 SVM 模型
# model = SVC(kernel='rbf', C=20, gamma='scale', random_state=42)
# model.fit(X_train_scaled, y_train)

# # 预测与评估
# y_pred = model.predict(X_test_scaled)
# acc = accuracy_score(y_test, y_pred)
# print(f"\n>>> 【HOG+HSV+SVM】测试准确率: {acc:.4f} ({acc*100:.2f}%)")

# print("\n=== 分类报告 ===")
# print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# # 可视化混淆矩阵
# conf_matrix = confusion_matrix(y_test, y_pred)
# plt.figure(figsize=(8, 6))
# sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
# plt.ylabel('True Label')
# plt.xlabel('Predicted Label')
# plt.title('Confusion Matrix')
# plt.show()

# # 可视化部分测试集样本及其预测结果
# def plot_sample_predictions(images, true_labels, pred_labels, num_samples=5):
#     indices = np.random.choice(len(images), num_samples, replace=False)
#     fig, axes = plt.subplots(1, num_samples, figsize=(15, 3))
#     for i, idx in enumerate(indices):
#         ax = axes[i]
#         ax.imshow(images[idx])
#         ax.set_title(f'True: {true_labels[idx]}\nPred: {pred_labels[idx]}')
#         ax.axis('off')
#     plt.tight_layout()
#     plt.show()

# # 将预测标签转换回原始类别名
# y_test_names = label_encoder.inverse_transform(y_test)
# y_pred_names = label_encoder.inverse_transform(y_pred)

# # 可视化部分测试集样本及其预测结果
# plot_sample_predictions(X_test.reshape(-1, *IMG_SIZE, 3), y_test_names, y_pred_names)