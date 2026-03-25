import cv2 
import numpy as np

img_path = r""

# 图像以灰度图输入(两种方式，不经过转换)

# img=cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)#以灰度模式读取图像
img=cv2.imread(img_path,0)#以灰度模式读取图像

# 图像放缩
src = cv2.resize(img, (256,256))

#图像的直方图
cal=cv2.calcHist(src, [0], None, [256],[0,256])  

# 灰度图均衡化
equ=cv2.equalizeHist(src)

# 水平拼接原图和均衡图
result = np.hstack((src, equ))

# 打印结果
print(np.sum(equ)) 

cv2.imshow('equ',equ)
cv2.imshow('result',result)
cv2.waitKey(0)                # 按任意键继续
cv2.destroyAllWindows()       # 关闭所有OpenCV窗口

