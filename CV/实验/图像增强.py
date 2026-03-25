import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
from scipy.fft import fft2, fftshift, ifft2, ifftshift # 导入FFT函数


# MSE函数
def calculate_mse(imageA, imageB):
    # 确保图像是浮点数以避免整数溢出
    imageA = imageA.astype(np.float64)
    imageB = imageB.astype(np.float64)
    # 计算均方误差
    err = np.sum((imageA - imageB) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

# 读取图像
image = cv2.imread(r"", cv2.IMREAD_GRAYSCALE)
image_ref = cv2.imread(r"", cv2.IMREAD_GRAYSCALE)

# 高斯滤波
gauss_image = cv2.GaussianBlur(image,(5,5),0) # 卷积核大小(5, 5)

# 计算高斯滤波后的图像质量指标
mse_gauss = calculate_mse(image_ref, gauss_image)
psnr_gauss = psnr(image_ref, gauss_image)
ssim_gauss = ssim(image_ref, gauss_image, data_range=gauss_image.max() - gauss_image.min())
print(f"Gaussian Blur - MSE: {mse_gauss}, PSNR: {psnr_gauss}, SSIM: {ssim_gauss}")

# 显示图像
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Blurred Image (Gauss Filtering)')
plt.imshow(gauss_image, cmap='gray')
plt.axis('off')

plt.show()


# 傅里叶变换
f = fft2(image)
fshift = fftshift(f)

# 设计低通滤波器
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2
radius = 30 # 滤波器半径
mask = np.zeros((rows, cols), np.uint8)
cv2.circle(mask, (ccol, crow), radius, (1, 1, 1), -1)
fshift_filtered = fshift * mask

# 逆傅里叶变换
f_ishift = ifftshift(fshift_filtered)
img_back = ifft2(f_ishift)
img_back = np.abs(img_back)

# 显示图像
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Filtered Image (Low-pass)')
plt.imshow(img_back, cmap='gray')
plt.axis('off')

plt.show()

# 显示参考图像
plt.title('References Image')
plt.imshow(image_ref,cmap='gray')
plt.axis('off')

plt.show()


# 计算低通滤波后的图像质量指标
mse_gauss = calculate_mse(image_ref, img_back)
psnr_lowpass = psnr(image_ref, img_back)
ssim_lowpass = ssim(image_ref, img_back, data_range=img_back.max() - img_back.min())
 
print(f"Low-pass Filter - MSE: {mse_gauss}, PSNR: {psnr_lowpass}, SSIM: {ssim_lowpass}")