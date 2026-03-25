import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread(r"")

# 转换为灰度图
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 高斯滤波去除噪声
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# 显示处理后图像
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Gray Image')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Blurred Image')
plt.imshow(blurred_image, cmap='gray')
plt.axis('off')

plt.show()

# Otsu阈值分割(适用灰度图像,双峰分布,自动阈值计算)
ret, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 显示分割结果
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title('Preprocessed Image')
plt.imshow(blurred_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Otsu Segmentation')
plt.imshow(binary_image, cmap='gray')
plt.axis('off')

plt.show()

# 计算分割区域的面积
mask = binary_image // 255 # 将二值图像转换为布尔掩码[0, 1]
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    area = cv2.contourArea(contour)  # 计算面积
    perimeter = cv2.arcLength(contour, True)  # 计算闭合轮廓的周长
    x, y, w, h = cv2.boundingRect(contour)  # 获取边界框
    circularity = (4 * 3.14 * area) / (perimeter * perimeter)  # 圆度计算
    
    print(f'Area: {area}, Perimeter: {perimeter}, Bounding Box: ({x}, {y}, {w}, {h}), Circularity: {circularity}')
    print()

# 读取标注图像
an_image = cv2.imread(r'', cv2.IMREAD_GRAYSCALE)

# 确保标注图像是二值化的
_, an_binary_image = cv2.threshold(an_image, 75, 255, cv2.THRESH_BINARY)

# 显示标注图像
plt.figure(figsize=(8, 4))
plt.title('Annotated Image')
plt.imshow(an_binary_image, cmap='gray')
plt.axis('off')
plt.show()

# 计算交集和并集
intersection = cv2.bitwise_and(binary_image, an_binary_image)
union = cv2.bitwise_or(binary_image, an_binary_image)

# 计算IoU
intersection_area = np.sum(intersection > 0)
union_area = np.sum(union > 0)
iou = intersection_area / union_area if union_area != 0 else 0.0

print(f'IoU: {iou:.4f}')

# 显示对比图像
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Segmentation Result')
plt.imshow(binary_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Annotated Image')
plt.imshow(an_binary_image, cmap='gray')
plt.axis('off')

plt.show()

# Canny边缘检测
edges = cv2.Canny(blurred_image, 30, 90)

# 形态学操作（膨胀）
kernel = np.ones((3, 3), np.uint8)
dilated_edges = cv2.dilate(edges, kernel, iterations=1)

# 查找轮廓
contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
segmented_image = np.zeros_like(image)
cv2.drawContours(segmented_image, contours, -1, (0, 255, 0), thickness=cv2.FILLED)

# 显示分割结果
plt.figure(figsize=(8, 4))
plt.title('Segmentation using Edge Detection and Morphology')
plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
print(f"Number of contours found: {len(contours)}")