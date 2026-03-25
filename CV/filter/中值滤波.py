import numpy as np
import cv2
img_path=r""
########Begin########
# 图像输入
img=cv2.imread(img_path)

# 图像放缩
img = cv2.resize(img, (256, 256))

# 中值滤波
median = cv2.medianBlur(img, 5)
########End########
cv2.imshow('median',median)

# 打印像素总和  
print('像素总和:',np.sum(median))  
# 打印平均像素值  
print('平均像素值:',np.mean(median))  
# 打印标准差  
print('标准差:',np.std(median)) 

cv2.waitKey(0)                # 按任意键继续
cv2.destroyAllWindows()       # 关闭所有OpenCV窗口