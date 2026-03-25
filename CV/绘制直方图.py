import cv2
import matplotlib.pyplot as plt
import matplotlib

img = cv2.imread(r"")
# 绘制出该图片 r, g, b 不同通道的直方图
# 使用 opencv 的方法进行绘制
# 绘图颜色由该通道颜色决定
# x 轴范围设置为 0 ~ 256

matplotlib.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号

hist_b=cv2.calcHist([img], [0], None, [256], [0,256]) 
hist_g=cv2.calcHist([img], [1], None, [256], [0,256])
hist_r=cv2.calcHist([img], [2], None, [256], [0,256])

plt.figure()
plt.title("grayhist")
# 设置X轴标签
plt.xlabel("bins")
# 设置Y轴标签
plt.ylabel("fixels")

plt.plot(hist_b, color='blue')
plt.plot(hist_g, color='green')
plt.plot(hist_r, color='red')

plt.xlim([0, 255])  # 设置 x 轴范围
plt.show()
plt.close()

