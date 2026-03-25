import numpy as np
import cv2

img_path = r""
########Begin########
# 图像输入
src = cv2.imread(img_path)
# 图像放缩
img = cv2.resize(src, (256, 256))
# 高斯滤波  ksize=(5,5),sigmaX=0
guass = cv2.GaussianBlur(img,(5,5),0)
########End########
cv2.imshow('guass',guass)
# 打印像素总和  
print('像素总和:',np.sum(guass))  
# 打印平均像素值  
print('平均像素值:',np.mean(guass))  
 # 打印标准差  
print('标准差:',np.std(guass)) 

cv2.waitKey(0)                # 按任意键继续
cv2.destroyAllWindows()       # 关闭所有OpenCV窗口