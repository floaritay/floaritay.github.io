from skimage import data,exposure
import matplotlib.pyplot as plt

img=data.moon()
plt.figure("hist",figsize=(8,8))

arr=img.flatten() # 将图像展平为一维数组
plt.subplot(221)
plt.imshow(img,plt.cm.gray)  #原始图像

plt.subplot(222)
plt.hist(arr, bins=256, density=True,edgecolor='None',facecolor='red') #原始图像直方图
# bins=256：将像素值范围（0-255）分为256个区间。
# density=True：归一化直方图（面积总和为1）。
# edgecolor='None'：无边框颜色。
# facecolor='red'：直方图填充颜色为红色。

# 直方图均衡化
img1=exposure.equalize_hist(img)
arr1=img1.flatten()
plt.subplot(223)
plt.imshow(img1,plt.cm.gray)  #均衡化图像
plt.subplot(224)
plt.hist(arr1, bins=256, density=True,edgecolor='None',facecolor='red') #均衡化直方图
plt.show()
