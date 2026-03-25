from skimage import data
from matplotlib import pyplot as plt
image=data.coffee()  # 载入测试图像
ratio=2               # 设置量化比率
for i in range(image.shape[0]): # 遍历图像的每个像素位置(i, j)和每个颜色通道(k)
    for j in range(image.shape[1]):
        for k in range(image.shape[2]):
            image[i][j][k]=int(image[i][j][k]/ratio)*ratio
            # 对图像每个像素进行量化
            # 若ratio=4，100会被量化为int(100/4)*4=100，但102会量化为100，103也会量化为100
plt.imshow(image)#打印采样后图像图像
plt.show()
