import cv2 
img_path=img_path=r""
img=cv2.imread(img_path)


# 任务1 高斯平滑，高斯卷积核的大小，宽，高为 (3,3)，标准差为1 
img_gauss = cv2.GaussianBlur(img,(3,3),1)
    

# 任务2 均值平滑，使用opencv的boxFilter()函数和blur()函数进行均值平滑
# boxFilter()函数均值平滑深度为-1，宽高(3,5)
# blur()函数均值平滑，宽高(3,5)
img_boxFilter = cv2.boxFilter(img,-1,(3,5))
img_blur = cv2.blur(img,(3,5))


# 任务3 中值平滑，核的大小，格式为5
img_medianblur = cv2.medianBlur(img,5)


# 任务4 双边滤波，卷积核的领域直径0，颜色空间滤波器标准偏差值0.2，坐标空间中滤波器标准偏差值40
img_bilateral = cv2.bilateralFilter(img,0,0.2,40)


cv2.imshow("Original", img)
cv2.imshow("GaussianBlur", img_gauss)
cv2.imshow("BoxFilter", img_boxFilter)
cv2.imshow("Blur", img_blur)
cv2.imshow("Median Blur", img_medianblur)
cv2.imshow("BilateralFilter", img_bilateral)
cv2.waitKey(0)                # 按任意键继续
cv2.destroyAllWindows()       # 关闭所有OpenCV窗口