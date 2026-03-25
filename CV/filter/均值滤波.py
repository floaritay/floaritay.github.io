# 算术均值滤波
import cv2
import numpy as np

# 使用opencv读取灰度图
image = cv2.imread("zao.png", cv2.IMREAD_GRAYSCALE)
# 待输出的图片
output = np.zeros(image.shape, np.uint8)#用于创建一个指定形状和数据类型的数组，并将所有元素初始化为零。
    #image.shape 返回的是输入图像的维度信息.例如，如果图像的尺寸是 500x500 像素，则 image.shape 将返回 (500, 500)
    #np.uint8 表示无符号8位整数，取值范围是 0 到 255

# 遍历图像，进行均值滤波
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
    #image.shape[0] 获取的是图像的高度
    #image.shape[1] 获取的是图像的宽度 
    #假设一个灰度图像 image，其尺寸为 500x500 像素，则 image.shape 将返回 (500, 500)
        # 滤波器内像素值的和
        sum = 0
        # 遍历滤波器内的像素值
        for m in range(-1, 2):
        #遍历以当前像素 (i, j) 为中心的垂直方向上的偏移量
            for n in range(-1, 2):
            # 水平方向上的偏移量    
                # 防止越界
                if 0 <= i + m < image.shape[0] and 0 <= j + n < image.shape[1]:
                    # 像素值求和
                    sum += image[i + m][j + n]
        # 求均值，作为最终的像素值
        output[i][j] = int(sum / 9)# 除以9的话会不会因为越界产生偏差？
# 展示均值滤波后的图片
cv2.imshow("after filter.png", output)
# 等待用户的键盘输入
cv2.waitKey()


# 几何均值滤波器
# 几何均值滤波器的思想是在给定窗口内的像素值计算几何均值。几何均值是所有数值的乘积的n次方根，其中n是数值的数量
import numpy as np
import cv2
import math

# 使用opencv读取图片
image = cv2.imread("/data/workspace/myshixun/step2/原图/zao.png", cv2.IMREAD_GRAYSCALE)
# 待输出的图片
output = np.zeros(image.shape, np.uint8)
# 遍历图像，进行均值滤波
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        ji = 1.0 #  初始化几何均值变量
        ######### Begin #########
        # 遍历滤波器内的像素值，滤波器的大小为1*3
        for n in range(-1,2):
            if 0 <= j + n < image.shape[1]:
                #算数值累乘
                ji *= image[i][j + n]
                # count += 1
        output[i][j] = int(math.pow(ji,1.0/3))#计算一个数的幂,ji的1/3次方           
        ######### End #########
# 展示均值滤波后的图片
cv2.imwrite("/data/workspace/myshixun/step2/学员文件/output.png", output)
# 等待用户的键盘输入
print(output)
print(np.sum(output))