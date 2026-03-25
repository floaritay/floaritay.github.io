# 本图片有周期性彩色条纹，故采用频率域去噪
# 频率域去噪	周期性条纹、全局规律噪声	精准去除特定频率成分	计算复杂，可能丢失高频细节
# 空间域去噪	局部条纹、非周期性噪声	    算法简单，实时性高	    可能模糊图像细节
# 频谱图中心代表低频成分，边缘代表高频成分
# 周期性噪声在频谱图中表现为明亮的斑点或线条，通常对称分布在中心周围
      
# 周期性条纹在傅里叶频谱中表现为亮斑（高频能量集中），通过构造频率域掩膜抑制这些亮斑对应的频率成分，即可精准去除条纹。
# 中心十字：代表低频成分（图像整体亮度）
# 亮斑/亮线：代表周期性噪声的频率成分
# 对称性：傅里叶频谱具有共轭对称性，噪声通常成对出现

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像并转为灰度图
image = cv2.imread(r"", cv2.IMREAD_GRAYSCALE)

# 进行傅里叶变换
f = np.fft.fft2(image) # 傅里叶变换
fshift = np.fft.fftshift(f) # 将低频移动到中心（低频位于频谱的四个角落）

# 创建一个低通滤波器掩模
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2 # 中心点
mask = np.zeros((rows, cols), np.uint8)
radius = 30  # 滤波器半径
cv2.circle(mask, (ccol, crow), radius, 1, thickness=-1)  # 圆形低通滤波器
# 使用 cv2.circle 在掩模中心绘制一个半径为 radius 的圆形区域，值为 1，表示保留的低频区域。
# thickness=-1 表示填充圆形。

# 应用掩模。值为 1 的区域保留低频成分，值为 0 的区域抑制高频成分。
fshift = fshift * mask

# 反傅里叶变换
ishift = np.fft.ifftshift(fshift) # 将低频移回原位置
img_back = np.fft.ifft2(ishift) # 反傅里叶变换
img_back = np.abs(img_back) # 取复数的绝对值，得到实数图像

# 显示结果
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(image)
 
plt.subplot(1, 3, 2)
plt.title("Frequency Domain ")
magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)  # 频谱图，20*lgK
plt.imshow(magnitude_spectrum)
 
plt.subplot(1, 3, 3)
plt.title("Filtered Image")
plt.imshow(img_back)
 
plt.tight_layout()# 自动调整子图之间的间距
plt.show()