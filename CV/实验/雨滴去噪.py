import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

# 读取图像
left_image = cv2.imread(r"")
right_image = cv2.imread(r"")

# 灰度化
gray_left_image = cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY)
gray_right_image = cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)

# 噪声去除（中值滤波）
denoised_left_image = cv2.medianBlur(gray_left_image, 5)
denoised_right_image = cv2.medianBlur(gray_right_image, 5)

# 显示图像
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Original Left Image')
plt.imshow(cv2.cvtColor(left_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Gray Left Image')
plt.imshow(gray_left_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Denoised Left Image')
plt.imshow(denoised_left_image, cmap='gray')
plt.axis('off')

plt.show()

# 类似地显示右图像
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Original Right Image')
plt.imshow(cv2.cvtColor(right_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Gray Right Image')
plt.imshow(gray_right_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Denoised Right Image')
plt.imshow(denoised_right_image, cmap='gray')
plt.axis('off')

plt.show()

# 自适应阈值分割
thresh_left_image = cv2.adaptiveThreshold(denoised_left_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                         cv2.THRESH_BINARY_INV, 11, 2)
thresh_right_image = cv2.adaptiveThreshold(denoised_right_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY_INV, 11, 2)

# 形态学操作（闭运算）优化水滴区域检测
kernel = np.ones((5, 5), np.uint8)
closed_left_image = cv2.morphologyEx(thresh_left_image, cv2.MORPH_CLOSE, kernel)
closed_right_image = cv2.morphologyEx(thresh_right_image, cv2.MORPH_CLOSE, kernel)

# 去除水滴信息（填充操作）
# 注意：实际可能需要更复杂的算法来保留图像细节，可以使用inpainting等更高级的方法
mask_left_image = cv2.bitwise_not(closed_left_image)
inpainted_left_image = cv2.inpaint(gray_left_image, closed_left_image, 3, cv2.INPAINT_TELEA)

mask_right_image = cv2.bitwise_not(closed_right_image)
inpainted_right_image = cv2.inpaint(gray_right_image, closed_right_image, 3, cv2.INPAINT_TELEA)

# 显示图像
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Thresholded Left Image')
plt.imshow(thresh_left_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Closed Left Image')
plt.imshow(closed_left_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Inpainted Left Image')
plt.imshow(inpainted_left_image, cmap='gray')
plt.axis('off')

plt.show()

# 类似地处理右图像
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Thresholded Right Image')
plt.imshow(thresh_right_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Closed Right Image')
plt.imshow(closed_right_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Inpainted Right Image')
plt.imshow(inpainted_right_image, cmap='gray')
plt.axis('off')

plt.show()

# 读取标准图像
truth_left_image = cv2.imread(r"")
truth_right_image = cv2.imread(r"")
# 转为灰度图，确保维度一致
truth_left_image = cv2.cvtColor(truth_left_image, cv2.COLOR_BGR2GRAY)
truth_right_image = cv2.cvtColor(truth_right_image, cv2.COLOR_BGR2GRAY)
# 计算 SSIM 和 PSNR
ssim_left = ssim(truth_left_image, inpainted_left_image, data_range=inpainted_left_image.max() - inpainted_left_image.min())
psnr_left = psnr(truth_left_image, inpainted_left_image, data_range=inpainted_left_image.max() - inpainted_left_image.min())

ssim_right = ssim(truth_right_image, inpainted_right_image, data_range=inpainted_right_image.max() - inpainted_right_image.min())
psnr_right = psnr(truth_right_image, inpainted_right_image, data_range=inpainted_right_image.max() - inpainted_right_image.min())

# 打印评估结果
print(f"Left Image - SSIM: {ssim_left:.4f}, PSNR: {psnr_left:.2f} dB")
print(f"Right Image - SSIM: {ssim_right:.4f}, PSNR: {psnr_right:.2f} dB")