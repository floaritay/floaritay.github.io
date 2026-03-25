from skimage import io  #导入io模块，用于图像的读取
from matplotlib import pyplot as plt #用于图像的显示
import numpy as np #用于数组和矩阵运算

image_path = r""
image = io.imread(image_path)  #载入测试图像
print(image.shape)  #显示图像原始大小
print(type(image))  #显示图像类型

plt.figure(figsize=(10, 5))#创建了一个新的图形窗口，其大小为10英寸宽和5英寸高。figsize参数用于指定图形的大小
plt.subplot(1, 2, 1)#将图形窗口分割成一个1行2列的子图网格，并激活第1个子图作为当前绘图区域,(1, 2, 1)分别表示行数、列数和当前子图的索引号
plt.title('Original Image')#这行代码为当前激活的子图设置标题为“Original Image”
plt.imshow(image)#imshow函数在当前激活的子图中显示图像。image是要显示的灰度图像数组
plt.axis('off')#关闭当前子图的坐标轴

ratio=10    #设置采样比率(缩放因子) 下采样，减少分辨率
image1=np.zeros((int(image.shape[0]/ratio),
                 int(image.shape[1]/ratio),image.shape[2]),dtype='int32')
# image.shape[0] 是图像的高度(行数)
# image.shape[1] 是图像的宽度(列数)
# 颜色通道数不变
#指定了新数组 image1 的数据类型为32位整数

for i in range(image1.shape[0]): # 遍历新图像的高度
    for j in range(image1.shape[1]):# 遍历新图像的宽度
        for k in range(image1.shape[2]):# 遍历颜色通道(对于彩色图像是3，对于灰度图像是1)
            # delta 是从原始图像 image 中提取的一个局部块
            # 尺寸是 ratio x ratio，并且位于 (i*ratio, j*ratio) 到 ((i+1)*ratio, (j+1)*ratio) 之间，
            # 对于当前遍历到的颜色通道 k。
            delta=image[i*ratio:(i+1)*ratio,j*ratio:(j+1)*ratio,k]#获取需要采样图像块
            # np.mean(delta) 计算了 delta 中所有像素值的均值，
            # 然后将这个均值赋值给新图像 image1 中对应位置 (i, j, k) 的像素。
            image1[i,j,k]=np.mean(delta) # 计算均值，并存入结果图像

# 量化操作：将均值四舍五入到0-255范围内，并转换为uint8类型
image1 = np.clip(np.round(image1), 0, 255).astype(np.uint8)# image1已经是整数了，np.round(image1) 将返回与 image1 相同的数组
# np.round 函数对其应用四舍五入操作,np.clip 函数用于将数组中的值限制在 0 到 255 的范围内,astype(np.uint8) 方法将数组的数据类型从 int32 转换为 uint8
# uint8 类型是无符号的 8 位整数，能够表示从 0 到 255 的值，这是存储和显示标准 8 位图像数据
# 减少了图片的细节或分辨率。下采样过程中，通过合并相邻像素的值来减少图像的像素数量，从而导致图像的分辨率降低,使得图像看起来更加模糊或不够清晰

plt.subplot(1, 2, 2)
plt.imshow(image1)#打印采样后图像图像
plt.title('Processing Image')
plt.imshow(image1)
plt.axis('off')

plt.show()



# 量化通常指的是将连续的数值范围映射到有限的离散级别上。在图像处理中，量化通常用于将像素值从浮点数(或具有更高精度的整数)转换为具有较低精度(和更少级别)的整数表示
# pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple