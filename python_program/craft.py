import cv2
import numpy as np
from matplotlib import pyplot as plt #用于图像的显示

# 读取图像并分通道处理
image_path=r""
image=cv2.imread(image_path)
median = cv2.medianBlur(image, 7)
gauss = cv2.GaussianBlur(image,(5,5),1)

cv2.imshow('median',median)
cv2.imshow('gauss',gauss)
cv2.imwrite(r"", gauss)
cv2.waitKey(0)                # 按任意键继续
cv2.destroyAllWindows()       # 关闭所有OpenCV窗口
print('Processing completed and result saved.')