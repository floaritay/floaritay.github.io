import cv2
from skimage.morphology import skeletonize
from matplotlib import pyplot as plt
import numpy as np

image=cv2.imread(r"")
image_gray=cv2.imread(r"",0)
# image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Canny边缘检测
edges_canny = cv2.Canny(image_gray, 50, 150) # 低阈值 高阈值 在这两个阈值之间的像素，则只有在其与超过高阈值的像素连接时，才会被视为边缘的一部分

# Sobel算子
sobelx = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=3)
# 计算梯度幅度
edges_sobel = np.sqrt(sobelx**2 + sobely**2).astype(np.uint8)
# cv2.CV_64F：指定输出图像的数据类型为64位浮点数。使用浮点数是为了能够表示负数梯度值，因为导数可以是正数也可以是负数
# 1, 0：分别表示在X方向上的导数阶数和Y方向上的导数阶数。这里设置为1, 0意味着只计算X方向上的导数
# ksize=3：Sobel核的大小。默认是3，意味着使用一个3x3的Sobel核进行卷积操作

# Laplacian算子
edges_laplacian = cv2.Laplacian(image_gray, cv2.CV_64F)
edges_laplacian = np.uint8(np.abs(edges_laplacian)) # Laplacian变换可能生成带有负号的结果

# 将三种边缘检测结果进行融合
edges_fused = cv2.addWeighted(edges_canny, 0.5, edges_sobel, 0.25, 0) # 加权融合函数，用于将两张图片按照各自的权重叠加
# 0.5：edges_canny图像的权重，表示在最终融合结果中该图像的重要性占比
# 0.25：edges_sobel图像的权重，在最终结果中的重要性占比
# 0：标量附加值，通常为0，表示不额外增加亮度或对比度。
edges_fused = cv2.addWeighted(edges_fused, 0.75, edges_laplacian, 0.25, 0)

# 骨架化处理
skeleton = skeletonize(edges_fused > 0).astype(np.uint8) * 255 # 骨架化函数
# edges_fused > 0：布尔运算，所有非零像素（即被识别为边缘的像素）都会被设为True(或1)
# 乘以255,原本值为1的位置现在变成了255


# 显示原始图像和各种边缘检测结果
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(edges_canny, cmap='gray')
plt.title('Canny Edges')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(edges_sobel, cmap='gray')
plt.title('Sobel Edges')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(edges_laplacian, cmap='gray')
plt.title('Laplacian Edges')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(edges_fused, cmap='gray')
plt.title('Fused Edges')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(skeleton, cmap='gray')
plt.title('Skeletonized Edges')
plt.axis('off')

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()