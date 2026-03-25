# 采样是将连续的二维空间信号（如模拟图像）转换为离散像素点（数字图像）的过程
# 量化是将采样后的像素值（通常是连续的灰度或颜色值）映射为有限数量的离散值的过程
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image_path =r""
image = io.imread(image_path)

# 参数设置
sampling_ratios = [2, 4, 8]  # 采样间隔
quantization_levels_list = [64, 128, 256]  # 量化级别

# 函数：采样图像
def sample_image(image, ratio):
    return image[::ratio, ::ratio]

# 函数：量化图像
def quantize_image(image, quantization_levels):
    max_val = 255
    quantized_image = np.round((image / max_val) * (quantization_levels - 1)).astype(np.uint8) * (max_val / (quantization_levels - 1))
    return quantized_image

# 显示采样效果
def show_sampling(gray_image):
    plt.figure(figsize=(12, 4))
    for i, ratio in enumerate(sampling_ratios):
        sampled_image = sample_image(gray_image, ratio)
        plt.subplot(1, len(sampling_ratios), i + 1)
        plt.title(f'Sample {ratio}')
        plt.imshow(sampled_image, cmap='gray')
        plt.axis('off')
    plt.tight_layout()
    plt.show()

# 显示量化效果
def show_quantization(gray_image):
    plt.figure(figsize=(15, 5))
    for i, quantization_levels in enumerate(quantization_levels_list):
        quantized_image = quantize_image(gray_image, quantization_levels)
        plt.subplot(1, len(quantization_levels_list), i + 1)
        plt.title(f'Quant {quantization_levels}')
        plt.imshow(quantized_image, cmap='gray')
        plt.axis('off')
    plt.tight_layout()
    plt.show()

# 显示采样效果
print("Sampling Effects on Gray Image:")
show_sampling(image)

# 显示量化效果
print("\nQuantization Effects on Gray Image:")
show_quantization(image)

# 热力图
plt.figure(figsize=(8, 6))
plt.title('Heatmap of Image')
plt.imshow(image, cmap='hot') 
plt.colorbar() # 显示颜色条
plt.axis('off')
plt.show()

# 线性亮度变换
brightness_factor = 1.2 # 亮度因子
brightened_image = np.clip(image * brightness_factor, 0, 255).astype(np.uint8)

# 显示图像
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Brightened Image')
plt.imshow(brightened_image)
plt.axis('off')

plt.show()

