import matplotlib.pyplot as plt
from skimage.feature import graycomatrix, graycoprops
from skimage.color import rgb2gray, rgba2rgb
from skimage.io import imread
from skimage import img_as_ubyte
import numpy as np

# 1. 读取图像并转换为灰度图像
image = imread(r"")
# 该图片为RGBA，转为RGB
if image.shape[2] == 4:
    image = rgba2rgb(image)
# 转灰度图
gray_image = rgb2gray(image)
# 转uint8
gray_image_uint8 = img_as_ubyte(gray_image)

# 2. 选择感兴趣区域
region1 = gray_image_uint8[100:150, 100:150]
region2 = gray_image_uint8[200:250, 200:250]

# 3. 计算 GLCM 特征
def compute_glcm_features(image_patch):
    glcm = graycomatrix(
        image_patch,
        distances=[5],          # 像素对距离
        angles=[0, np.pi/4, np.pi/2, 3*np.pi/4],  #计算 4 个方向的纹理特征 0°, 45°, 90°, 135°
        levels=256,             # 灰度级（uint8 范围）
        symmetric=True,         # 对称矩阵
        normed=True             # 归一化（概率矩阵）
    )
    # 提取 4 种纹理特征
    contrast = graycoprops(glcm, 'contrast')       # 对比度（值越大，纹理越粗糙）
    correlation = graycoprops(glcm, 'correlation') # 相关性（值越大，像素间线性关系越强）
    energy = graycoprops(glcm, 'energy')           # 能量（值越大，纹理越均匀）
    homogeneity = graycoprops(glcm, 'homogeneity') # 同质性（值越大，局部变化越小）
    return contrast, correlation, energy, homogeneity

features_region1 = compute_glcm_features(region1)
features_region2 = compute_glcm_features(region2)

# 4. 可视化
fig = plt.figure(figsize=(20, 12))

# --- 第一部分：原始图像 + 标记的两个区域 ---
ax1 = plt.subplot2grid((3, 4), (0, 0), colspan=2)  ## 3行4列 第 1 行，占 2 列
ax1.imshow(image)
ax1.set_title("Original Image")
ax1.axis("off")
ax1.add_patch(plt.Rectangle((100, 100), 50, 50, fill=False, edgecolor='red', linewidth=2, label='Region 1'))
ax1.add_patch(plt.Rectangle((200, 200), 50, 50, fill=False, edgecolor='blue', linewidth=2, label='Region 2'))
ax1.legend(loc='upper right')

# --- 第二部分：Region 1 和 Region 2 的灰度图像 ---
ax2 = plt.subplot2grid((3, 4), (0, 2))  # 第 1 行，第 3 列
ax2.imshow(region1, cmap="gray")
ax2.set_title("Region 1 (Gray)")
ax2.axis("off")

ax3 = plt.subplot2grid((3, 4), (0, 3))  # 第 1 行，第 4 列
ax3.imshow(region2, cmap="gray")
ax3.set_title("Region 2 (Gray)")
ax3.axis("off")

# --- 第三部分：GLCM 特征可视化 GLCM 特征柱状图 ---
angles = ["0°", "45°", "90°", "135°"]
features = ["Contrast", "Correlation", "Energy", "Homogeneity"]

# Region 1 特征（第 2 行）
for i, feature in enumerate(features):
    ax = plt.subplot2grid((3, 4), (1, i))  # 第 2 行，第 i 列
    ax.bar(angles, features_region1[i][0], color='red', alpha=0.7)
    ax.set_title(f"Region 1: {feature}")
    ax.set_ylim(0, 1)

# Region 2 特征（第 3 行）
for i, feature in enumerate(features):
    ax = plt.subplot2grid((3, 4), (2, i))  # 第 3 行，第 i 列
    ax.bar(angles, features_region2[i][0], color='blue', alpha=0.7)
    ax.set_title(f"Region 2: {feature}")
    ax.set_ylim(0, 1)

plt.tight_layout()
plt.show()