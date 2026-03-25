import cv2
import numpy as np

# 读取图像
img_path1=r""
img1 = cv2.imread(img_path1)
img1_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)# 转换成HSV(色调，饱和度，亮度)
# 在 RGB 空间中，红色可能因为光照变化或阴影影响而难以准确检测，而在 HSV 空间中，可以通过设置色相范围来更精确地检测红色

# 定义红色范围
lower_red1 = np.array([0, 150, 50])
upper_red1 = np.array([3, 255, 150])
# H ∈ [0, 10]：色相值在 0 到 10 之间
# S > 50：饱和度值大于 50（避免检测到灰色或接近白色的区域）
# V > 50：亮度值大于 50（避免检测到黑色或接近黑色的区域）
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])
# H ∈ [170, 180]：色相值在 170 到 180 之间

# 创建掩膜
mask1 = cv2.inRange(img1_hsv, lower_red1, upper_red1)
# 使用 OpenCV 的 cv2.inRange() 函数，检测图像中属于该区间的像素。
# 返回值：
# mask1 是一个二值图像(掩膜)，其中：
# 如果某个像素的 HSV 值在 [lower_red1, upper_red1] 范围内，则该像素的值为 255（白色）。
# 否则，该像素的值为 0（黑色）。
mask2 = cv2.inRange(img1_hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)
# 使用 OpenCV 的 cv2.bitwise_or() 函数，将 mask1 和 mask2 合并为一个掩膜。
# 返回值：
# mask 是一个新的二值图像，其中：
# 如果某个像素在 mask1 或 mask2 中为 255（即属于第一个或第二个红色区间），则该像素在 mask 中为 255。
# 否则，该像素的值为 0。

# 替换红眼区域为棕色
img1_hsv[mask > 0] = [18, 74, 115]# BGR
# 转换回 RGB 空间
img1 = cv2.cvtColor(img1_hsv, cv2.COLOR_HSV2BGR)

# 显示结果
cv2.imshow('result_img', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()




 
# 读取图像
img_path2=r""
img2 = cv2.imread(img_path2)
img2_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
 
# 定义皮肤颜色范围
lower_skin1 = np.array([6, 0, 0])  
upper_skin1 = np.array([99, 255, 255])
 
# 创建掩膜
mask3 = cv2.inRange(img2_hsv, lower_skin1, upper_skin1)

# 替换皮肤区域为绿色
img2_hsv[mask3 > 0] = [50,255,100]  # 修改色调为绿色
 
# 转换回 RGB 空间
img2 = cv2.cvtColor(img2_hsv, cv2.COLOR_HSV2BGR)
 
# 显示结果
cv2.imshow('Green Skin ', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()