# 使用统计排序类滤波器时。首先需要定义滤波器的大小，比如3x3
# 然后，遍历图像中的每一个像素点，将滤波器覆盖上去，滤波器覆盖到的区域的像素值的最大值、最小值或者中间的值，用这些值替代原来的像素值
# 如果使用的是最大值，那就是最大值滤波器
# 如果使用的是最小值，那就是最小值滤波器
# 如果使用的是中值，那就是中值滤波器


# 中值滤波器的程序如下所示：


import cv2
import numpy as np
# 获取列表的中间值的函数
def get_middle(array):
    # 列表的长度
    length = len(array)
    # 对列表进行选择排序，获得有序的列表
    for i in range(length):
        for j in range(i + 1, length):
            # 选择最大的值
            if array[j] > array[i]:
                # 交换位置
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    return array[int(length/2)]
# 使用opencv读取灰度图
image = cv2.imread(r"", cv2.IMREAD_GRAYSCALE)
# 待输出的图片
output = np.zeros(image.shape, np.uint8)
# 存储滤波器范围内的像素值
array = []
# 遍历图像，进行中值滤波
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        # 清空滤波器内的像素值
        array.clear()
        # 遍历滤波器内的像素
        for m in range(-1, 2):# -1,0,1
            for n in range(-1, 2):
                # 防止越界
                if 0 <= i + m < image.shape[0] and 0 <= j + n < image.shape[1]:
                    # 像素值加到列表中
                    array.append(image[i + m][j + n])
        # 求中值，作为最终的像素值
        output[i][j] = get_middle(array)
# 展示原始图片和均值滤波后的图片
cv2.imshow('Original Image', image)
cv2.imshow("after filter", output)
# 等待用户的键盘输入
cv2.waitKey()
cv2.destroyAllWindows()




# 最大值滤波器的程序如下所示：


import numpy as np
import cv2
# 使用opencv读取图片
image = cv2.imread(r"", cv2.IMREAD_GRAYSCALE)
# 待输出的图片
output = np.zeros(image.shape, np.uint8)
def get_max(array):
    a=max(array)
    return a
array=[]
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        # 最大值滤波器,滤波器的大小是3*3
        array.clear()
        for m in range(-1,2):
             for n in range(-1, 2):
                 if 0 <= i + m < image.shape[0] and 0 <= j + n < image.shape[1]:
                    array.append(image[i + m][j + n])
        output[i][j] = get_max(array)

cv2.imshow('Original Image', image)
cv2.imshow("output",output)
print(output)#二维矩阵
print(np.sum(output))#二维矩阵的和
cv2.waitKey()
cv2.destroyAllWindows()
