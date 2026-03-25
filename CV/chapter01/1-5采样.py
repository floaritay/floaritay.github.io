from skimage import data
from matplotlib import pyplot as plt
import numpy as np 
image=data.coffee()  #载入测试图像
print(image.shape)  #显示图像原始大小
print(type(image))  #显示图像类型
ratio=20                #设置采样比率 原图像的每20×20像素块会被压缩为1个像素
image1=np.zeros((int(image.shape[0]/ratio),
                 int(image.shape[1]/ratio),image.shape[2]),dtype='int32')#设置采样后图像大小
# image1：初始化一个全零数组，用于存储采样后的图像。
# 尺寸：(原高度/ratio, 原宽度/ratio, 通道数)。
# 数据类型：int32（后续会存储均值计算结果）。

# 均值采样
for i in range(image1.shape[0]):
    for j in range(image1.shape[1]):
        for k in range(image1.shape[2]): # 遍历图像的每个像素位置(i, j)和每个颜色通道(k)
            delta=image[i*ratio:(i+1)*ratio,j*ratio:(j+1)*ratio,k]#获取需要采样图像块 20×20区域
            image1[i,j,k]=np.mean(delta)#计算均值，并存入结果图像
plt.imshow(image1)#打印采样后图像图像
plt.show()
