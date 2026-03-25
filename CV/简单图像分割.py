from skimage import data,filters, io,segmentation, color
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# 导入咖啡图片
coffee_image = data.coffee()
coffee_image_gray=cv2.cvtColor(coffee_image,cv2.COLOR_RGB2GRAY)

# 归一化的阈值
normalized_thresholds = [0.2, 0.5, 0.8]
 
# 将归一化的阈值映射到0-255的像素值
thresholds = [int(threshold * 255) for threshold in normalized_thresholds]
 
# 初始化用于显示分割结果的图像
segmented_images = []
 
# 根据每个阈值进行分割
for threshold in thresholds:
    # 创建一个二值图像，其中大于阈值的像素为255，其他为0
    segmented_image = (coffee_image_gray > threshold).astype(np.uint8) * 255
    segmented_images.append(segmented_image)
 
# 显示原始图像和分割后的图像
plt.figure(figsize=(15, 5))
 
plt.subplot(1, 4, 1)
plt.imshow(coffee_image_gray, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')
 
for i, segmented_image in enumerate(segmented_images, start=2):
    plt.subplot(1, 4, i)
    plt.imshow(segmented_image, cmap='gray')
    plt.title(f'Threshold > {normalized_thresholds[i-2]:.1f}')
    plt.axis('off')
 
plt.show()



# 使用Otsu方法计算阈值
threshold_otsu = filters.threshold_otsu(coffee_image_gray)
binary_image_otsu = coffee_image_gray > threshold_otsu
 
# 使用Niblack方法计算阈值
from skimage.filters import threshold_niblack
threshold_niblack = threshold_niblack(coffee_image_gray, window_size=15, k=0.2)
binary_image_niblack = coffee_image_gray > threshold_niblack
 
# 使用Sauvola方法计算阈值
from skimage.filters import threshold_sauvola
threshold_sauvola = threshold_sauvola(coffee_image_gray, window_size=15)
binary_image_sauvola = coffee_image_gray > threshold_sauvola
 
# 显示原始图像和分割后的图像
plt.figure(figsize=(15, 10))
 
plt.subplot(2, 2, 1)
plt.imshow(coffee_image_gray, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')
 
plt.subplot(2, 2, 2)
plt.imshow(binary_image_otsu, cmap='gray')
plt.title('Otsu Thresholding')
plt.axis('off')
 
plt.subplot(2, 2, 3)
plt.imshow(binary_image_niblack, cmap='gray')
plt.title('Niblack Thresholding')
plt.axis('off')
 
plt.subplot(2, 2, 4)
plt.imshow(binary_image_sauvola, cmap='gray')
plt.title('Sauvola Thresholding')
plt.axis('off')
 
plt.tight_layout()
plt.show()




# 初始化轮廓
# 这里使用一个矩形区域作为初始轮廓
# 参数 (y, x) 指定矩形的左上角和右下角
init_ls = np.zeros(coffee_image_gray.shape, dtype=np.int8)
init_ls[10:100, 10:100] = 1
 
# 使用Chan-Vese算法进行分割
segmented_image = segmentation.chan_vese(coffee_image_gray, max_num_iter=200, init_level_set=init_ls)
 
# 显示原始图像和分割后的图像
plt.figure(figsize=(10, 5))
 
plt.subplot(1, 2, 1)
plt.imshow(coffee_image_gray, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')
 
plt.subplot(1, 2, 2)
plt.imshow(segmented_image, cmap='gray')
plt.title('Chan-Vese Segmentation')
plt.axis('off')
 
plt.tight_layout()
plt.show()