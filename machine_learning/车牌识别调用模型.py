import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

# 设置字体为SimSun(宋体)
plt.rcParams['font.sans-serif'] = ['SimSun']
# 载入模型
model = tf.keras.models.load_model(r"...")
# 字符集
char_enum = ["京","沪","津","渝","冀","晋","蒙","辽","吉","黑","苏","浙","皖","闽","赣","鲁",
             "豫","鄂","湘","粤","桂","琼","川","贵","云","藏","陕","甘","青","宁","新","军","使"]
number   = [str(i) for i in range(0, 10)]
alphabet_upper = [chr(i) for i in range(65, 91)] # 大写字母A-Z
alphabet_lower = [chr(i) for i in range(97, 123)] # 小写字母a-z
char_set = char_enum + number + alphabet_upper + alphabet_lower # 合并所有字符，构成车牌可能的字符集合
# 将模型输出向量转换为字符串
def vec2text(vec):
    '''
    遍历模型输出的每个字符概率向量(vec[0])
    对每个字符的概率分布取最大值索引(np.argmax),映射到char_set中的字符。
    将字符拼接成字符串返回。
    '''
    text = []
    for i, c in enumerate(vec[0]):
        idx = np.argmax(c)
        text.append(char_set[idx])
    return "".join(text)
# 加载和处理图像文件
def load_and_preprocess_image(image_path):
    image = Image.open(image_path).convert('L')  # 转换为灰度图像
    image = image.resize((200, 50))  # 调整大小为模型输入大小
    image = np.array(image) / 255.0  # 归一化
    image = np.expand_dims(image, axis=-1)  # 添加批次维度
    return image

# # 获取用户输入的图像路径
# image_path = r"..."
# # 加载和处理图像
# plate_image = load_and_preprocess_image(image_path)
# # 使用模型进行预测
# predictions = model.predict(np.array([plate_image]))
# # 将模型输出向量转换为识别结果字符串
# recognized_plate_number = vec2text(predictions)
# # 打印识别结果
# print("识别结果：", recognized_plate_number)
# # 显示输入车牌图片和识别结果的对比
# plt.figure(figsize=(8, 4))
# plt.subplot(1, 2, 1)
# plt.imshow(plate_image[:, :, 0], cmap='gray')
# plt.title('输入车牌图片')
# plt.axis('off')
# plt.subplot(1, 2, 2)
# plt.bar(range(len(recognized_plate_number)), predictions[0, :, :].max(axis=1), color='blue', label='识别结果概率')
# plt.xticks(range(len(recognized_plate_number)), recognized_plate_number)
# plt.xlabel('车牌号码')
# plt.ylabel('概率')
# plt.title('车牌号码识别结果')
# plt.legend()
# plt.tight_layout()
# plt.show()


# 获取文件夹路径
folder_path = r"..."
 
# 遍历文件夹中的所有文件
with os.scandir(folder_path) as entries:
    for entry in entries:
        if entry.is_file():  # 确保是文件
            image_path = entry.path  # 获取完整路径
            try:
                # 加载和处理图像
                plate_image = load_and_preprocess_image(image_path)
                # 使用模型进行预测
                predictions = model.predict(np.array([plate_image]))
                # 将模型输出向量转换为识别结果字符串
                recognized_plate_number = vec2text(predictions)
                # 打印识别结果
                print("识别结果：", recognized_plate_number)
                
                # 显示输入车牌图片和识别结果的对比
                plt.figure(figsize=(8, 4))
                plt.subplot(1, 2, 1)
                plt.imshow(plate_image[:, :, 0], cmap='gray')
                plt.title('输入车牌图片')
                plt.axis('off')
                plt.subplot(1, 2, 2)
                plt.bar(range(len(recognized_plate_number)), predictions[0, :, :].max(axis=1), color='blue', label='识别结果概率')
                plt.xticks(range(len(recognized_plate_number)), recognized_plate_number)
                plt.xlabel('车牌号码')
                plt.ylabel('概率')
                plt.title('车牌号码识别结果')
                plt.legend()
                plt.tight_layout()
                plt.show()
            except Exception as e:
                print(f"处理文件 {entry.name} 时出错: {e}")