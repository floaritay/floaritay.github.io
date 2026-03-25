import sys
import cv2 
import matplotlib.pyplot as plt
import numpy as np

#计算直方图函数,img参数为输入图像,img_plt为生成图像灰度直方图
def histCover(img):
    plt.figure('hist', figsize=(16, 8))
    # 展示输入图像
    plt.subplot(121)
    plt.imshow(img, "gray")
    # 展示直方图
    plt.subplot(122)
    """
    任务1 利用cv2.calcHist()内置函数进行画灰度图像直方图,该函数的返回值是hist
    """    
    ########## Begin ##########
    hist=cv2.calcHist([img], [0], None, [256], [0,256])
    ########## End ##########
    print('max:',max(hist))
    print('min:',min(hist))
    plt.plot(hist)
    plt.xlim([0, 255])
    plt.show()

#主函数的定义,定义图片路径
def main_func(argv):
    img_path = r""
    """
    任务2. 读入图像,并转化为灰度值,数据路径已经给出为img_path
    """    
    ########## Begin ##########
    img=cv2.imread(img_path)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ########## End ##########
    """
    任务3. 调用histCover函数绘制直方图,看清楚该函数是无返回值的哦
    """
    ########## Begin ##########
    histCover(img_gray)
    ########## End ##########
if __name__ == '__main__':
    main_func(sys.argv)
