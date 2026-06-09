# 目录


---
# 基础模块
以下是 OpenCV 中最常用的一些模块：
  
- cv2.core: 核心模块，包含了图像处理的基础功能（如图像数组的表示和操作）

- cv2.imgproc: 图像处理模块，提供图像的各种操作，如滤波、图像变换、形态学操作等

- cv2.highgui: 图形用户界面模块，提供显示图像和视频的功能

- cv2.video: 提供视频处理的功能，如视频捕捉、视频流的处理等

- cv2.features2d: 特征检测与匹配模块，包含了角点、边缘、关键点检测等

- cv2.ml: 机器学习模块，提供了多种机器学习算法，可以进行图像分类、回归、聚类等

- cv2.calib3d : 相机校准和 3D 重建模块

- cv2.objdetect : 目标检测模块

- cv2.dnn : 深度学习模块

1. Core 模块  
功能: 提供 OpenCV 的核心功能，包括基本数据结构、矩阵操作、绘图函数等。  

主要类和函数:  

- Mat: OpenCV 中用于存储图像和矩阵的基本数据结构。

- Scalar: 用于表示颜色或像素值。

- Point、Size、Rect: 用于表示点、尺寸和矩形。

基本绘图函数: cv.line()、cv.circle()、cv.rectangle()、cv.putText() 等。   

应用场景:  图像的基本操作（如创建、复制、裁剪）。绘制几何图形和文本。  

2. Imgproc 模块  
功能: 提供图像处理功能，包括图像滤波、几何变换、颜色空间转换等。   

主要类和函数:  

- 图像滤波: cv.blur()、cv.GaussianBlur()、cv.medianBlur() 等。

- 几何变换: cv.resize()、cv.warpAffine()、cv.warpPerspective() 等。

- 颜色空间转换: cv.cvtColor()（如 BGR 转灰度、BGR 转 HSV）。

- 阈值处理: cv.threshold()、cv.adaptiveThreshold()。

- 边缘检测: cv.Canny()、cv.Sobel()、cv.Laplacian()。

应用场景:图像平滑、锐化、边缘检测。图像缩放、旋转、仿射变换。图像二值化、颜色空间转换。  

3. HighGUI 模块  
功能: 提供高层 GUI 和媒体 I/O 功能，用于图像的显示和交互。  

主要类和函数:  

- 图像显示: cv.imshow()、cv.waitKey()、cv.destroyAllWindows()。

- 视频捕获: cv.VideoCapture()、cv.VideoWriter()。

- 鼠标和键盘事件: cv.setMouseCallback()。

应用场景:显示图像和视频。捕获摄像头或视频文件。处理用户交互（如鼠标点击、键盘输入）。  

4. Video 模块  
功能: 提供视频分析功能，包括运动检测、目标跟踪等。  

主要类和函数:  

- 背景减除: cv.createBackgroundSubtractorMOG2()、cv.createBackgroundSubtractorKNN()。

- 光流法: cv.calcOpticalFlowPyrLK()。

- 目标跟踪: cv.TrackerKCF_create()、cv.TrackerMOSSE_create()。

应用场景:视频中的运动检测。目标跟踪（如行人、车辆跟踪）。

5. Calib3d 模块  
功能: 提供相机校准和 3D 重建功能。  

主要类和函数:

- 相机校准: cv.calibrateCamera()、cv.findChessboardCorners()。

- 3D 重建: cv.solvePnP()、cv.reprojectImageTo3D()。

应用场景:相机标定（用于去除镜头畸变）。3D 重建（如从 2D 图像恢复 3D 信息）。  

6. Features2d 模块
功能: 提供特征检测和描述功能。   

主要类和函数:  

- 特征检测: cv.SIFT_create()、cv.ORB_create()、cv.SURF_create()。

- 特征匹配: cv.BFMatcher()、cv.FlannBasedMatcher()。

- 关键点绘制: cv.drawKeypoints()。

应用场景:图像特征提取和匹配。图像拼接、物体识别。  

7. Objdetect 模块
功能: 提供目标检测功能。  

主要类和函数:  

- Haar 特征分类器: cv.CascadeClassifier()（用于人脸检测）。

- HOG 特征分类器: 用于行人检测。

应用场景:人脸检测、行人检测。  

8. ML 模块  
功能: 提供机器学习算法。  

主要类和函数:  

- 支持向量机 (SVM): cv.ml.SVM_create()。

- K 均值聚类 (K-Means): cv.kmeans()。

- 神经网络 (ANN): cv.ml.ANN_MLP_create()。

应用场景:图像分类、聚类分析。

9. DNN 模块  
功能: 提供深度学习功能，支持加载和运行预训练的深度学习模型。  

主要类和函数:

- 模型加载: cv.dnn.readNetFromCaffe()、cv.dnn.readNetFromTensorflow()。

- 前向传播: net.forward()。

应用场景:图像分类、目标检测、语义分割。

10. 其他模块  
Flann: 快速近似最近邻搜索。  

Photo: 图像修复和去噪。  

Stitching: 图像拼接。  

Shape: 形状匹配和距离计算。  

# 图像处理基础
图像的基本属性：  
- 图像的尺寸（Width, Height）：可以通过 img.shape 获取
- 颜色通道（Channels）：通常为 RGB（三个通道），也可以是灰度图（单通道）
- 数据类型（Data type）：常见的有 uint8（0-255 范围），也可以是 float32 或其他

## 基本操作
### imread()
### imshow()
### imwrite()
### destroyAllWindows()
### split()
### merge()


```python
import cv2
import numpy as np

image = cv2.imread('./bird.png') # 当前目录下的 "bird.jpg"，返回一个 NumPy 数组
# 读取图像并转为灰度图
img = cv2.imread('./bird.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('./bird.png', 0)

cv2.imshow('Image',image)

key = cv2.waitKey(0)    # 参数 0 表示无限等待，直到用户按下任意键

if key == ord('s'):
    cv2.imwrite('output_image',image)
    print(f"图像已保存为 'output_path' ")
else:
    print("图像未保存，程序已退出。")

cv2.destroyAllWindows()    
```


```python
## 访问和修改像素值
# 获取像素值 (BGR 格式)
pixel_value = image[100, 100]  # 获取 (100, 100) 处的像素值

# 修改像素值
image[100, 100] = [255, 255, 255]  # 将 (100, 100) 处的像素设置为白色

## 图像 ROI（Region of Interest）
# 获取 ROI
roi = image[50:150, 50:150]  # 获取 (50,50) 到 (150,150) 的区域

# 修改 ROI
image[50:150, 50:150] = [0, 255, 0]  # 将 ROI 区域设置为绿色

## 图像通道分离与合并
# 分离通道
b, g, r = cv2.split(image)

# 合并通道
merged_image = cv2.merge([b, g, r])
```

## 图像缩放、旋转、平移、翻转
### resize()
``resized_img = cv2.resize(img, (width, height))``
### getRotationMatrix2D()
``cv2.getRotationMatrix2D((center_x, center_y), angle, scale)``
### warpAffine()
``cv2.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) ``  
M：仿射变换矩阵，通常由cv2.getRotationMatrix2D获得  
dsize：输出图像的尺寸。需根据变换后的内容合理设置，避免裁剪  
flags（可选）：插值方法，影响变换后像素值的计算方式，默认值：cv2.INTER_LINEAR，常用选项：  
- cv2.INTER_NEAREST：最近邻插值（速度快，质量低）
- cv2.INTER_LINEAR：双线性插值（平衡速度与质量）
- cv2.INTER_CUBIC：三次样条插值（质量高，速度慢）
- cv2.INTER_LANCZOS4：Lanczos 插值（高质量，适合缩小图像）

borderMode（可选）：处理超出原图边界的像素的方式，默认值：cv2.BORDER_CONSTANT，常用选项：  
- cv2.BORDER_CONSTANT：用 borderValue 指定的值填充
- cv2.BORDER_REPLICATE：复制边界像素
- cv2.BORDER_REFLECT：反射边界像素

borderValue（可选）：默认值：(0, 0, 0)，当 borderMode=cv2.BORDER_CONSTANT 时，填充边界的像素值

### flip()
>```python
># 缩放
>resized_image = cv2.resize(image, (new_width, new_height))
>
># 旋转
>rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), angle, scale) 
># 旋转的中心点坐标（以图像像素坐标系为参考，原点 (0, 0) 在左上角）（中心点center = (img.shape[1] // 2, img.shape[0] // 2)）
># 旋转角度，正值表示逆时针旋转
># 缩放倍数
>rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
>
># 平移
>translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])  # 向右平移 tx 像素，向下平移 ty 像素
>translated_image = cv2.warpAffine(image, translation_matrix, (width, height))
>
># 翻转
>flipped_image = cv2.flip(image, flip_code)  # flip_code: 0 (垂直翻转), 1 (水平翻转), -1 (双向翻转)
>```

## 图像算术运算
### add()
如果像素值相加后超过 255，OpenCV 会自动将其截断为 255  
### subtract()
如果像素值相减后小于 0，OpenCV 会自动将其截断为 0  
### multiply()
如果像素值相乘后超过 255，OpenCV 会自动将其截断为 255
### devide()
如果除数为 0，OpenCV 会自动将结果设置为 0
### addWeighted()

>```python
># 1、图像加法
>result = cv2.add(image1, image2)
>
># 2、图像减法
>result = cv2.subtract(image1, image2)
>
># 3、图像混合
>result = cv2.addWeighted(image1, alpha, image2, beta, gamma)
># alpha 和 beta 是权重，gamma 是标量值。
>```

## 图像位运算
### cv2.bitwise_and()
掩码操作、图像分割
### cv2.bitwise_or()
图像叠加
### cv2.bitwise_not()
图像反色
### cv2.bitwise_xor() 按位异或
图像差异检测

>```python
># 位与运算
>result = cv2.bitwise_and(img1, img2)
>
># 位或运算
>result = cv2.bitwise_or(img1, img2)
>
># 位非运算
>result = cv2.bitwise_not(img1)
>
># 位异或运算
>result = cv2.bitwise_xor(img1, img2)

## 图像阈值处理
### threshold()
``cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst``  
type：阈值化类型
- cv2.THRESH_BINARY：超过阈值设为 maxval，否则为 0
- cv2.THRESH_BINARY_INV：超过阈值设为 0，否则为 maxval
- cv2.THRESH_TRUNC：超过阈值截断为阈值，否则保留原值
- cv2.THRESH_TOZERO：超过阈值保留原值，否则设为 0
- cv2.THRESH_TOZERO_INV：超过阈值设为 0，否则保留原值  

retval：实际使用的阈值（对 cv2.THRESH_OTSU 或 cv2.THRESH_TRIANGLE 等自适应阈值类型有效）  
输入图像类型：必须为灰度图
### adaptiveThreshold()
``cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) → dst``  
adaptiveMethod：局部阈值的计算方式  
- cv2.ADAPTIVE_THRESH_MEAN_C：阈值为局部邻域像素的均值减去常数 C  
- cv2.ADAPTIVE_THRESH_GAUSSIAN_C：阈值为局部邻域像素的高斯加权和减去常数 C  

thresholdType：与 cv2.threshold 中的类型一致   
blockSize：局部邻域的大小（奇数，如 3、5、11 等）。值越大，阈值计算受更大范围像素影响  
C：

>```python
>1、简单阈值处理
>ret, thresholded_image = cv2.threshold(image, thresh, maxval, cv2.THRESH_BINARY)
># thresh 是阈值，maxval 是最大值
>
>2、自适应阈值处理
>thresholded_image = cv2.adaptiveThreshold(image, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, C)
>
>3、Otsu 二值化
>ret, thresholded_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)# 自动计算最佳全局阈值（适用于双峰直方图图像）
>```

## 图像平滑处理
线性滤波函数（基于卷积核的加权平均）
### blur() 或 boxFilter() 
ksize：卷积核大小（如 (5,5)），必须为正奇数  
normalize（仅 boxFilter）：是否归一化核（默认 True，即均值计算；设为 False 可用于加权求和）
### GaussianBlur()
``cv2.GaussianBlur(src, ksize, sigmaX)``  
sigmaX（可选）：X方向标准差（控制权重分布，值越大越模糊；设为 0 时根据 ksize 自动计算）  
  
非线性滤波函数（基于像素排序或邻域关系）  
### medianBlur() 
``median_blurred = cv2.medianBlur(img, ksize)``  
ksize：卷积核大小（必须为正奇数，如 3、5）  
### bilateralFilter()
``bilateral_filtered = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)``
d：滤波邻域直径  
sigmaColor：颜色空间标准差（值越大，颜色混合范围越广）  
sigmaSpace：坐标空间标准差（值越大，空间影响范围越广）  

>```python
># 1、均值滤波
>blurred_image = cv2.blur(image, (kernel_size, kernel_size))
>
># 2、高斯滤波
>blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigmaX)
>
># 3、中值滤波
>blurred_image = cv2.medianBlur(image, kernel_size)
>
># 4、双边滤波
>blurred_image = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
>```

## 图像的颜色空间与转换
### cvtColor()
``cv2.cvtColor(src, code[, dstCn[, dst]])``  
code：颜色空间转换代码  
dstCn（可选）：输出图像的通道数。若未指定，则根据 code 自动推导

>```python
># 从 RGB 转换为灰度图：
>gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
>
># 从 BGR 转换为 HSV：
>hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
>
># 从 RGB 转换为 YUV：
>yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
>```

## 图像文本
### putText()
``cv2.putText(image, text, org, fontFace, fontScale, color, thickness)``
text: 要绘制的文本  

org: 文本左下角坐标  

fontFace: 字体类型（如 cv2.FONT_HERSHEY_SIMPLEX）  

fontScale: 字体缩放比例  

color: 文本颜色  

thickness: 文本线宽  

>```python
>import cv2
>
>img = cv2.imread('image.jpg')
>cv2.putText(img, 'Hello, OpenCV!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
>cv2.imshow('Text', img)
>cv2.waitKey(0)
>cv2.destroyAllWindows()
>```

## 图像边缘检测
### Canny()
Canny 算法原理：  
使用高斯滤波平滑图像以去除噪声。  
通过 Sobel 算子计算水平和垂直方向的梯度，进而得到梯度幅值和方向。  
通过非极大值抑制（NMS）保留梯度方向上的局部最大值，消除杂散响应，细化边缘。  
经过双阈值检测强边缘（梯度值 ≥ threshold2 的像素），弱边缘（threshold1 ≤ 梯度值 < threshold2 的像素），抑制孤立边缘（未与强边缘连接的弱边缘）    
  
``edges = cv2.Canny(image, threshold1, threshold2[, apertureSize[, L2sobelient]])``  
image：输入图像，必须为单通道灰度图（数据类型为 uint8）  
threshold1：低阈值，用于边缘连接。梯度值低于此值的像素被抑制  
threshold2：高阈值，用于边缘检测。梯度值高于此值的像素被视为强边缘  
apertureSize（可选）：Sobel 算子的大小，默认为 3（可选值为 3、5、7）  
L2sobelient（可选）：布尔值，默认为 False，使用 L1 范数计算梯度幅值（计算更快）。若为 True，则使用 L2 范数（更精确但计算量更大）  

### Sobel()
``edges = cv2.Sobel(src, ddepth, dx, dy[, ksize[, scale[, delta[, borderType]]]])``
src：输入图像，必须为单通道灰度图  
ddepth（输出图像深度）：
- cv2.CV_8U：8 位无符号整数（0~255），但会截断负值，可能导致梯度信息丢失
- cv2.CV_16S：16 位有符号整数（-32768~32767），推荐使用，可保留完整梯度值
- cv2.CV_32F/cv2.CV_64F：32/64 位浮点数，适用于高精度计算

dx 和 dy（导数阶数）:指定求导方向：
- dx=1, dy=0：计算 x 方向梯度（检测垂直边缘）。
- dx=0, dy=1：计算 y 方向梯度（检测水平边缘）。

避免同时设为 1（如 dx=1, dy=1），否则结果可能不符合预期。若需合并方向梯度，可分别计算后通过 cv2.addWeighted() 合并

ksize（Sobel 核大小）:卷积核尺寸，必须为奇数（如 1、3、5、7）。默认值为 3  
scale（缩放因子）:默认值为 1。若需放大梯度值（如增强边缘亮度），可设置 scale > 1  
delta（偏移量）:默认值为 0。计算结果会加上此值，常用于调试或调整亮度  
borderType（边界处理方式）:默认值为 cv2.BORDER_DEFAULT
- cv2.BORDER_DEFAULT：镜像填充
- cv2.BORDER_CONSTANT：填充固定值（如黑色）。
- cv2.BORDER_REPLICATE：复制边缘像素。

### Laplacian()
``dst = cv2.Laplacian(src, ddepth[, ksize[, scale[, delta[, borderType]]]])``  
src：输入图像，必须为单通道灰度图（数据类型为 uint8 或 float32）  
ksize：近似核尺寸，必须为正奇数（如 1、3、5）。默认值为 1  
其他参数参考Sobel()  

### Scharr()
  
>```python
># Canny 边缘检测：
>edges = cv2.Canny(img, 100, 200)
># Canny 算法通过对图像进行梯度计算来找出边缘，返回一个二值图像，边缘处为白色，其他区域为黑色
># 低阈值过低：导致噪声被误检为边缘
># 高阈值过高：导致真实边缘丢失
>
># Sobel 算子：
>sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
>sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
>sobel_y_abs = cv2.convertScaleAbs(sobel_y)
>sobel_x_abs = cv2.convertScaleAbs(sobel_x)
># 合并梯度（加权平均）
>grad_combined = cv2.addWeighted(grad_x_abs, 0.5, grad_y_abs, 0.5, 0)
>
># Laplacian 算子：
>laplacian = cv2.Laplacian(image, cv2.CV_64F)
>laplacian_abs = cv2.convertScaleAbs(laplacian)
># 显示结果
>cv2.imshow('Laplacian Edges', laplacian_abs)
>```


```python
# 滑动条交互式调整阈值，观察边缘检测效果
import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread(r"C:\Users\LENOVO\Pictures\Saved Pictures\1679907039016722.jpg", cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Canny Demo')
cv2.createTrackbar('Threshold1', 'Canny Demo', 0, 255, nothing)
cv2.createTrackbar('Threshold2', 'Canny Demo', 0, 255, nothing)

while True:
    t1 = cv2.getTrackbarPos('Threshold1', 'Canny Demo')
    t2 = cv2.getTrackbarPos('Threshold2', 'Canny Demo')
    edges = cv2.Canny(img, t1, t2)
    cv2.imshow('Canny Demo', edges)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
```

## 形态学操作
形态学操作常用于二值图像的处理，常见的操作有腐蚀、膨胀、开运算、闭运算等。   
### getStructuringElement()
``kernel = cv2.getStructuringElement(shape, ksize[, anchor])``  
shape：指定结构元素的几何类型   
- cv2.MORPH_RECT：矩形核（所有像素值为 1）
- cv2.MORPH_ELLIPSE：椭圆形核
- cv2.MORPH_CROSS：交叉形核
  
ksize：指定核的尺寸，格式为 (width, height)，必须为正奇数 如 (3, 3)、(5, 5)   
若需动态调整核大小，可通过循环实现 for i in range(1, 5): kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * i + 1, 2 * i + 1))    

anchor（锚点位置）：指定核的中心点坐标，默认值为 (-1, -1)，表示自动计算中心  

kernel：返回一个 numpy.ndarray 类型的二值矩阵（0 和 1），表示结构元素的形状  

### erode()
``dst = cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) ``  

src：输入图像，通常是二值化（黑白）或灰度图像  

kernel：结构元素（Structuring Element），用于定义腐蚀操作的邻域形状  

anchor（可选）：结构元素的锚点位置，默认为中心 (-1, -1)  

iterations（可选）：腐蚀操作的次数，默认为 1。次数越多，腐蚀效果越强  

### dilate()
``dst = cv2.dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])``  
### morphologyEx()
``dst = cv2.morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])``  

src：输入图像，支持二值图像（黑白）或灰度图像

op：形态学操作类型
- cv2.MORPH_ERODE：腐蚀（等同于 cv2.erode()）

- cv2.MORPH_DILATE：膨胀（等同于 cv2.dilate()）

- cv2.MORPH_OPEN：开运算（先腐蚀后膨胀，用于去除小噪点）

- cv2.MORPH_CLOSE：闭运算（先膨胀后腐蚀，用于填补空洞）

- cv2.MORPH_GRADIENT：形态学梯度（膨胀图减去腐蚀图，突出边缘）

- cv2.MORPH_TOPHAT：礼帽（原图减去开运算结果，提取亮细节）

- cv2.MORPH_BLACKHAT：黑帽（闭运算结果减去原图，提取暗细节）


>```python
>
>kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
># 腐蚀（Erosion）：将图像中的白色区域收缩
>eroded_img = cv2.erode(img, kernel, iterations=1)
>
># 膨胀（Dilation）：将图像中的白色区域扩展
>dilated_img = cv2.dilate(img, kernel, iterations=1)
>
># 开运算与闭运算：
># 开运算（先腐蚀再膨胀）：用于去除小物体
># 闭运算（先膨胀再腐蚀）：用于填补图像中的小孔洞
>opening_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
>closing_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
>```

## 图像轮廓检测
OpenCV 提供了强大的轮廓检测功能，可以用于对象识别、图像分割等应用
### findContours()
``contours, hierarchy = cv2.findContours(image, mode, method, offset=None)``  

image：必须是黑白图像，通常通过阈值处理 或 边缘检测生成  

mode（轮廓检索模式）：定义如何检索轮廓的层级关系（适用于嵌套轮廓，如环形物体）  

- cv2.RETR_EXTERNAL：只检测最外层轮廓，忽略内部嵌套轮廓。适用于简单物体计数或外边界提取

- cv2.RETR_LIST：检测所有轮廓，不建立层级关系（所有轮廓是平级的）。适用于无需分析轮廓嵌套关系的场景

- cv2.RETR_CCOMP：检测所有轮廓，但只建立两层层级（外层和内层）。适用于有简单嵌套结构的物体（如文字中的字母和标点）

- cv2.RETR_TREE：检测所有轮廓，并建立完整的层级树（父子关系）。适用于复杂嵌套结构（如俄罗斯套娃、细胞团）  
  
method（轮廓近似方法）：定义如何存储轮廓点（平衡精度与效率）   

- cv2.CHAIN_APPROX_NONE：存储轮廓的所有点（可能包含冗余点）。适用于需要精确轮廓的场景（如测量边缘长度）

- cv2.CHAIN_APPROX_SIMPLE：压缩水平、垂直和对角方向的冗余点，仅保留端点（如矩形轮廓仅存储4个角点）。适用于大多数场景（减少内存占用，提高处理速度）

- cv2.CHAIN_APPROX_TC89_L1 / cv2.CHAIN_APPROX_TC89_KCOS：基于 Teh-Chin 链逼近算法，更精确地逼近曲线轮廓。适用于需要高精度轮廓的场景（如医学图像分析）  

offset（可选偏移量）：如果轮廓是从图像的某个子区域提取的，可通过 offset=(dx, dy) 调整轮廓坐标，使其匹配原图位置。默认值为 (0, 0)（无偏移）   

contours：检测到的轮廓列表，每个轮廓是一个 NumPy 数组，形状为 (N, 1, 2)，其中 N 是轮廓点数  

hierarchy：轮廓的层级关系矩阵，形状为 (1, N, 4)，其中 N 是轮廓数量。  
每个轮廓的层级信息包含 [Next, Previous, First_Child, Parent]：  

- Next：同层级的下一个轮廓索引（-1 表示无）

- Previous：同层级的上一个轮廓索引（-1 表示无）

- First_Child：第一个子轮廓索引（-1 表示无）

- Parent：父轮廓索引（-1 表示无）

### drawContours()
``cv2.drawContours(image, contours, contourIdx, color, thickness=-1)``   
image：指定在哪张图像上绘制轮廓（可以是原图、副本或空白图像）   
注意：函数会直接修改此图像，若需保留原图，请先复制一份 如 img_copy = img.copy()   

contours（轮廓列表）：通常由 cv2.findContours() 返回   

contourIdx（轮廓索引）：指定绘制哪个轮廓：    

- -1：绘制所有轮廓（常用）

- 0, 1, 2...：绘制指定索引的轮廓 

color（轮廓颜色）：BGR 格式，如 (255, 0, 0) 表示蓝色  
注意：若在灰度图上绘制，颜色需为单通道值（如 255 表示白色）  

thickness（线条宽度）：  

- 大于0：绘制轮廓线（值越大线越粗）  
 
- -1（或 cv2.FILLED）：填充轮廓内部区域  

### contourArea()
``area = cv2.contourArea(contour[, oriented])`
### arcLength()
``length = cv2.arcLength(curve, closed)``计算轮廓的周长或弧长  
closed: 布尔值，表示轮廓是否闭合  
### boundingRect()
``x, y, w, h = cv2.boundingRect(points)``计算轮廓的边界矩形  
返回边界矩形的左上角坐标 (x, y) 和宽度 w、高度 h  
### minAreaRect()
``rect = cv2.minAreaRect(points)``计算轮廓的最小外接矩形  
返回一个旋转矩形，包含中心点 (x, y)、宽度、高度和旋转角度  
### minEnclosingCircle()
``(center, radius) = cv2.minEnclosingCircle(points)``计算轮廓的最小外接圆  
返回圆心 (x, y) 和半径 radius  
### approxPolyDP()
``approx = cv2.approxPolyDP(curve, epsilon, closed)``对轮廓进行多边形近似  
epsilon: 近似精度，值越小，近似越精确  
closed: 布尔值，表示轮廓是否闭合  
返回近似后的多边形点集  
>```python
># 检测轮廓：
>gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
>_ , threshold_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
>_ , contours= cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
>
>for contour in contours:
>    #面积
>    area = cv2.contourArea(contour)
>    print(f"Contour area: {area}")
>    # 周长或弧长
>    perimeter = cv2.arcLength(contour, True)
>    print(f"Contour perimeter: {perimeter}")
>    # 边界矩形
>    x, y, w, h = cv2.boundingRect(contour)
>    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
>    # 最小外接矩
>    rect = cv2.minAreaRect(contour)
>    box = cv2.boxPoints(rect)
>    box = box.astype(int)
>    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
>    # 最小外接圆
>    (x, y), radius = cv2.minEnclosingCircle(contour)
>    center = (int(x), int(y))
>    radius = int(radius)
>    cv2.circle(img, center, radius, (255, 0, 0), 2)
>    # 多边形近似轮廓
>    epsilon = 0.01 * cv2.arcLength(contour, True)
>    approx = cv2.approxPolyDP(contour, epsilon, True)
>    cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
>
># 绘制轮廓：
>cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
>cv2.imshow('Contours', img)
>
>cv2.waitKey(0)
>cv2.destroyAllWindows()
>```


```python
import cv2
import numpy as np
 
# 读取图像并二值化
image = cv2.imread('shapes.png', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 检测所有轮廓并建立层级关系
contours, hierarchy = cv2.findContours(
    binary, 
    cv2.RETR_TREE, 
    cv2.CHAIN_APPROX_SIMPLE
)
 
# 绘制轮廓（不同颜色区分层级）
result = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
for i, contour in enumerate(contours):
    color = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
    cv2.drawContours(result, contours, i, color, 2)
    # 打印层级信息
    h = hierarchy[0][i]
    print(f"Contour {i}: Parent={h[3]}, Children={h[2]}")
 
cv2.imshow('Hierarchical Contours', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## 图像直方图
OpenCV 提供了丰富的直方图计算和操作函数：

|功能	        |函数	                     |   说明|
|---|---|---|
|计算直方图	    |cv2.calcHist()	            |计算图像的直方图|
|直方图均衡化	|cv2.equalizeHist()	        |增强图像的对比度|
|直方图比较	    |cv2.compareHist()	        |比较两个直方图的相似度|

### calcHist()
``hist = cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])``  
images: 输入的图像列表，通常是一个包含单通道或多通道图像的列表。例如 [img]  

channels: 需要计算直方图的通道索引。对于灰度图像，使用 [0]；对于彩色图像，可以使用 [0]、[1]、[2] 分别计算蓝色、绿色和红色通道的直方图  

mask: 掩码图像。如果指定了掩码，则只计算掩码区域内的像素。如果不需要掩码，可以传入 None  

histSize: 直方图的 bin 数量。对于灰度图像，通常设置为 [256]，表示将灰度级分为 256 个 bin  

ranges: 像素值的范围。对于灰度图像，通常设置为 [0, 256]，表示像素值的范围是 0 到 255  

hist: 输出的直方图数组  

accumulate: 是否累积直方图。如果设置为 True，则直方图不会被清零，而是在每次调用时累积  

### equalizeHist()
``equalized_image = cv2.equalizeHist(image)``

### normalize()
``dst = cv2.normalize(src, dst=None, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=-1)``
norm_type：归一化类型。

- cv2.NORM_MINMAX	线性归一化到 [alpha, beta] 区间。

- cv2.NORM_INF	按无穷范数（最大绝对值）缩放，使最大值为 alpha。

- cv2.NORM_L1	按 L1 范数（绝对值之和）缩放，使 L1 范数为 alpha。

- cv2.NORM_L2	按 L2 范数（欧几里得距离）缩放，使 L2 范数为 alpha。

- cv2.NORM_RELATIVE	相对归一化（较少使用，需结合其他范数）。

- cv2.NORM_MINMAX + cv2.NORM_RELATIVE	相对线性归一化（需结合具体场景）。

dtype（可选）：整数（如 cv2.CV_32F、cv2.CV_8U）。若为负数（默认），则与输入类型相同

### compareHist()
``similarity = cv2.compareHist(hist1, hist2, method)``  
method: 比较方法，例如 cv2.HISTCMP_CORREL（相关性比较）  


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread(r"C:\Users\LENOVO\Pictures\Saved Pictures\1679907039016722.jpg", cv2.IMREAD_GRAYSCALE)

# 计算直方图
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# 绘制直方图
plt.plot(hist)
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

# 直方图均衡化
equalized_image = cv2.equalizeHist(img)
# 显示结果
cv2.imshow("Equalized Image", equalized_image)

# 读取彩色图像
image = cv2.imread(r"C:\Users\LENOVO\Pictures\Saved Pictures\1679907039016722.jpg")

# 计算 BGR 各通道的直方图
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)

# 绘制直方图
plt.title("Color Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Pixel Count")
plt.show()

# 分离通道
b, g, r = cv2.split(image)

# 对每个通道进行直方图均衡化
b_eq = cv2.equalizeHist(b)
g_eq = cv2.equalizeHist(g)
r_eq = cv2.equalizeHist(r)

# 合并通道
equalized_image = cv2.merge([b_eq, g_eq, r_eq])

# 显示结果
cv2.imshow("Equalized Color Image", equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

## 视频处理
OpenCV 也支持视频的处理，可以读取视频文件、捕捉视频流并进行实时处理  
### VideoCapture()
``cv2.VideoCapture(source)``
### VideoWriter()
``cv2.VideoWriter(filename, fourcc, fps, frameSize)``  

fourcc: 视频编码器  如 cv2.VideoWriter_fourcc(*'XVID')  

fps: 帧率  

frameSize: 帧大小（宽度, 高度）  
### cap.isOpened()
### cap.read()	
逐帧读取视频
### cap.get(propId)	
获取视频的属性（如宽度、高度、帧率等）
### TrackerKCF_create()
使用目标跟踪算法跟踪视频中的物体
### createBackgroundSubtractorMOG2()
使用背景减除算法检测视频中的运动物体


```python
# 读取并播放一个视频文件，同时允许用户通过按键（q）提前终止播放   waitKey 的延迟时间（毫秒）影响播放速度（1 表示尽可能快，25 约 40 FPS）

cap = cv2.VideoCapture('video.mp4') # 将 'video.mp4' 替换为 0 即可调用摄像头

# 检查视频是否成功打开
while cap.isOpened():
    ret, frame = cap.read() # ret：布尔值，表示是否成功读取帧。frame：当前帧的图像数据
    # 如果读取到最后一帧，退出循环
    if not ret:
        break
    # 处理每一帧,将帧转换为灰度图像
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Video', gray_frame)
    # 等待 1 毫秒，返回按键的 ASCII 码（若无按键则返回 -1）。& 0xFF：确保兼容 64 位系统（屏蔽高位字节）
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    
cap.release() # 释放视频捕获对象，关闭文件或摄像头连接，防止资源泄漏
cv2.destroyAllWindows()
```


```python
cap = cv2.VideoCapture('example.mp4')

# 获取视频的帧率和尺寸
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建 VideoWriter 对象，保存处理后的视频
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # 将帧转换为灰度图像
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 将灰度帧写入输出视频
    out.write(cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR))
    
    # 显示灰度帧
    cv2.imshow('Gray Video', gray_frame)
    
    delay = int(1000 / fps)         # 计算每帧延迟（毫秒）
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
```

# 运动检测
运动检测是视频处理中的一个重要应用。可以通过计算帧之间的差异来检测运动物体  

以下是一个简单的运动检测示例：


```python
import cv2

cap = cv2.VideoCapture('example.mp4')

# 读取第一帧
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # 将当前帧转换为灰度图像
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 计算当前帧与前一帧的差异
    frame_diff = cv2.absdiff(prev_gray, gray_frame)
    
    # 对差异图像进行二值化处理
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
    
    # 显示运动检测结果
    cv2.imshow('Motion Detection', thresh)
    
    # 更新前一帧
    prev_gray = gray_frame
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

# 视频目标跟踪
MeanShift（均值漂移）算法是一种基于密度的非参数化聚类算法，最初用于图像分割，后来被引入到目标跟踪领域。  
其核心思想是通过迭代计算目标区域的质心，并将窗口中心移动到质心位置，从而实现目标的跟踪。  

MeanShift 算法的基本步骤如下：
1. 初始化窗口：在视频的第一帧中，手动或自动选择一个目标区域，作为初始窗口。

2. 计算质心：在当前窗口中，计算目标区域的质心（即像素点的均值）。

3. 移动窗口：将窗口中心移动到质心位置。

4. 迭代：重复步骤 2 和 3，直到窗口中心不再变化或达到最大迭代次数。

优点：
- 简单易实现，计算效率高。

- 对目标的形状和大小变化不敏感。

缺点：
- 对目标的快速运动或遮挡处理能力较差。

- 窗口大小固定，无法自适应目标大小的变化。

CamShift（Continuously Adaptive MeanShift）算法是 MeanShift 的改进版本，它通过自适应调整窗口大小来更好地跟踪目标。  
CamShift 算法在 MeanShift 的基础上增加了窗口大小和方向的调整，使其能够适应目标在视频中的尺寸和旋转变化。  

CamShift 算法的基本步骤如下：  
1. 初始化窗口：与 MeanShift 相同，在视频的第一帧中选择初始窗口。

2. 计算质心：在当前窗口中，计算目标区域的质心。

3. 移动窗口：将窗口中心移动到质心位置。

4. 调整窗口大小和方向：根据目标的尺寸和方向调整窗口。

5. 迭代：重复步骤 2 到 4，直到窗口中心不再变化或达到最大迭代次数。

优点：
- 能够自适应目标的大小和方向变化。

- 对目标的形状变化和旋转具有较好的鲁棒性。

缺点：
- 对目标的快速运动或遮挡处理能力仍然有限。

- 计算复杂度略高于 MeanShift。

## meanShift()
``retval, window = cv2.meanShift(probImage, window, criteria)``  

probImage：输入图像（单通道，8位或32位浮点）表示目标概率分布的图像（通常通过反向投影生成）。例如，使用 cv2.calcBackProject() 计算目标颜色的直方图反向投影

window：元组 (x, y, w, h)。初始搜索窗口，指定跟踪区域的矩形，左上角坐标 (x,y) 和宽高 (w,h)

criteria：终止条件（cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT）

retval：达到终止条件前的迭代次数

window：跟踪结束后目标所在的矩形窗口位置和大小

反向投影：将目标颜色直方图映射到当前帧，生成概率图像 probImage

``backProject = cv2.calcBackProject(images, channels, hist, ranges, scale[, dst])``  

images：输入图像或图像列表（单通道或多通道，如 BGR 图像需拆分通道）。

channels：整数列表。指定参与计算的图像通道索引。例如，HSV 颜色空间的 [0] 表示色调（Hue），[1] 表示饱和度（Saturation）。

hist：直方图（numpy.ndarray 或 cv2.Mat）。目标特征的直方图模型（需预先计算并归一化）。例如，通过 cv2.calcHist() 计算目标区域的颜色直方图，再用 cv2.normalize() 归一化。

ranges：浮点数列表（如 [0, 180, 0, 256]）。每个通道的取值范围。例如，HSV 空间的色调范围为 [0, 180]，饱和度范围为 [0, 256]。

scale：浮点数（默认 1.0）。输出概率图的缩放因子。若需将概率值映射到 [0, 255]，可设为 255


```python
import cv2
import numpy as np

# 读取视频
cap = cv2.VideoCapture('video.mp4')

# 读取第一帧
ret, frame = cap.read()

# 设置初始窗口 (x, y, width, height)
x, y, w, h = 300, 200, 100, 50
track_window = (x, y, w, h)

# 设置 ROI (Region of Interest)
roi = frame[y:y+h, x:x+w]

# 转换为 HSV 颜色空间
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# 创建掩膜并计算直方图
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
roi_hist = cv2.normalize(roi_hist, 0, 255, cv2.NORM_MINMAX)

# 设置终止条件
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1) # 最大迭代次数 10。窗口中心移动的最小阈值 1 像素

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 转换为 HSV 颜色空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 计算反向投影
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # 应用 MeanShift 算法
    ret, track_window = cv2.meanShift(dst, track_window, term_crit)

    # 绘制跟踪结果
    x, y, w, h = track_window
    img2 = cv2.rectangle(frame, (x, y), (x+w, y+h), 255, 2)
    cv2.imshow('MeanShift Tracking', img2)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
```

## CamShift()
``retval, rotated_rect = cv2.CamShift(probImage, window, criteria)``

probImage：单通道输入图像，通常是反向投影图，由 cv2.calcBackProject() 生成。表示目标颜色分布的概率图，像素值越高，属于目标的概率越大。

window：初始搜索窗口（第一帧由用户手动指定）。

criteria：终止条件（TermCriteria），通常设置为 (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)，表示迭代最多 10 次或当窗口移动小于 1 像素时停止。

retval：一个旋转矩形，包含：中心点坐标（x, y）。自适应调整后的窗口尺寸大小（width, height）。旋转角度（angle）。


```python
import cv2
import numpy as np

# 读取视频
cap = cv2.VideoCapture('video.mp4')

# 读取第一帧
ret, frame = cap.read()

# 设置初始窗口 (x, y, width, height)
x, y, w, h = 300, 200, 100, 50
track_window = (x, y, w, h)

# 设置 ROI (Region of Interest)
roi = frame[y:y+h, x:x+w]

# 转换为 HSV 颜色空间
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# 创建掩膜并计算直方图
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# 设置终止条件
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 转换为 HSV 颜色空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 计算反向投影
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # 应用 CamShift 算法
    ret, track_window = cv2.CamShift(dst, track_window, term_crit)

    # 绘制跟踪结果
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    img2 = cv2.polylines(frame, [pts], True, 255, 2)
    cv2.imshow('CamShift Tracking', img2)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
```

# 视频背景减除
背景减除的核心思想是通过建模背景，然后将当前帧与背景模型进行比较，从而分离出前景对象。

OpenCV 提供了多种背景减除算法，其中 MOG（Mixture of Gaussians）和 MOG2 是最常用的两种方法。

MOG（Mixture of Gaussians）算法

MOG 算法是一种基于高斯混合模型（Gaussian Mixture Model, GMM）的背景减除方法。其核心思想是使用多个高斯分布来建模背景中的像素值。  
每个像素的值被看作是一个随机变量，其分布由多个高斯分布组成。通过这种方式，MOG 能够处理背景中的复杂变化，如光照变化、阴影等。

算法步骤
1. 初始化：为每个像素初始化多个高斯分布。

2. 模型更新：对于每一帧图像，更新每个像素的高斯分布参数（均值、方差、权重）。

3. 前景检测：将当前帧的像素值与背景模型中的高斯分布进行比较，如果像素值不在任何高斯分布的范围内，则将其标记为前景。

MOG2（Mixture of Gaussians Version 2）算法

MOG2 是 MOG 的改进版本，主要区别在于它能够自动选择高斯分布的数量，并且能够更好地适应背景的变化。  
MOG2 通过动态调整高斯分布的数量和参数，能够更准确地建模背景，从而提高前景检测的准确性。

算法步骤
1. 初始化：为每个像素初始化多个高斯分布。

2. 模型更新：对于每一帧图像，更新每个像素的高斯分布参数，并根据需要增加或减少高斯分布的数量。

3. 前景检测：将当前帧的像素值与背景模型中的高斯分布进行比较，如果像素值不在任何高斯分布的范围内，则将其标记为前景。

MOG 算法通过固定数量的高斯分布来建模背景，适用于背景变化较少的场景，  
而 MOG2 算法通过动态调整高斯分布的数量和参数，能够更好地适应背景的变化，适用于背景变化较多的场景。

## bgsegm.createBackgroundSubtractorMOG()
``mog = cv2.bgsegm.createBackgroundSubtractorMOG()``  
``mog.apply()``


```python
import cv2

# 创建 MOG 背景减除器
mog = cv2.bgsegm.createBackgroundSubtractorMOG()

# 读取视频
cap = cv2.VideoCapture('video.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 应用背景减除
    fg_mask = mog.apply(frame)

    # 显示结果
    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fg_mask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## createBackgroundSubtractorMOG2()
``mog2 = cv2.createBackgroundSubtractorMOG2()``
``mog2.apply()``


```python
import cv2

# 创建 MOG2 背景减除器
mog2 = cv2.createBackgroundSubtractorMOG2()

# 读取视频
cap = cv2.VideoCapture('video.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 应用背景减除
    fg_mask = mog2.apply(frame)

    # 显示结果
    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fg_mask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

# 物体检测
OpenCV 提供了多种物体检测算法，如 Haar 特征分类器、HOG + SVM 等   
OpenCV 提供了基于 Haar 特征分类器的人脸检测方法，简单易用且效果显著   

Haar 特征分类器是一种基于 Haar-like 特征的机器学习方法。  
它通过提取图像中的 Haar-like 特征，并使用 AdaBoost 算法进行训练，最终生成一个分类器，用于检测图像中的目标（如人脸）。

Haar-like 特征是一种简单的矩形特征，通过计算图像中不同区域的像素值差异来提取特征。  
例如，一个 Haar-like 特征可以是两个相邻矩形的像素值之和的差值。这些特征能够捕捉到图像中的边缘、线条等结构信息。

OpenCV 中的 Haar 特征分类器  
OpenCV 提供了预训练的 Haar 特征分类器，可以直接用于人脸检测。这些分类器以 XML 文件的形式存储，包含了训练好的模型参数。

OpenCV 中的 cv2.CascadeClassifier() 类用于加载和使用这些分类器。

人脸检测的实现步骤  
1. 加载 Haar 特征分类器模型: 使用 cv2.CascadeClassifier() 加载预训练的人脸检测模型。

2. 读取图像: 使用 cv2.imread() 读取待检测的图像。

3. 转换为灰度图: 将图像转换为灰度图，因为 Haar 特征分类器在灰度图上运行更快。

4. 检测人脸: 使用 detectMultiScale() 方法检测图像中的人脸。

5. 绘制检测结果: 在图像中绘制检测到的人脸矩形框。

6. 显示结果: 显示检测结果。

## CascadeClassifier()
``classifier = cv2.CascadeClassifier(xml_path)``    

>```python
>objects = classifier.detectMultiScale(
>    image,              # 输入图像  必须是灰度图   
>    scaleFactor=None,   # （可选）：图像缩放比例（默认 1.1）。值越小，检测越精细（但计算量更大）
>    minNeighbors=None,  # （可选）：控制检测质量的参数（默认 3）。值越大，假阳性越少，但可能漏检 
>    minSize=None,       # （可选）：对象的最小尺寸  如 (30, 30)
>    maxSize=None        # （可选）：对象的最大尺寸
>)
>```


```python
import cv2

# 加载 Haar 特征分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 读取图像
image = cv2.imread('image.jpg')

# 转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 进行人脸检测
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 绘制检测结果
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# 显示结果
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```


```python
import cv2

# 加载 Haar 特征分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture('example.mp4')

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # 将帧转换为灰度图像
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 检测人脸
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # 在帧上绘制矩形框标记人脸
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # 显示带有人脸标记的帧
    cv2.imshow('Face Detection', frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

# 物体识别
什么是模板匹配？
模板匹配是一种在图像中寻找与给定模板图像最相似区域的技术。

简单来说，模板匹配就是在一幅大图像中寻找与模板图像（即我们想要识别的物体）最匹配的部分，这种方法适用于物体在图像中的大小、方向和形状基本不变的情况。

- 模板图像: 目标物体的图像片段。

模板匹配的基本原理  
模板匹配的基本原理是通过滑动模板图像在目标图像上移动，计算每个位置的相似度，并找到相似度最高的位置。  
OpenCV 提供了多种相似度计算方法，如

|计算方法|说明|匹配度|
|---|---|---|
|cv2.TM_SQDIFF|平方差匹配|值越小匹配度越高|
|cv2.TM_SQDIFF_NORMED|归一化平方差匹配，对光照变化更鲁棒||
|cv2.TM_CCORR|相关匹配，计算模板与图像的乘积和|值越大匹配度越高|
|cv2.TM_CCORR_NORMED|归一化相关匹配，消除亮度影响||
|cv2.TM_CCOEFF|相关系数匹配|值越大匹配度越高|
|cv2.TM_CCOEFF_NORMED|归一化相关系数匹配，对光照和对比度变化更鲁棒（推荐）||
  
应用场景
- 物体识别: 用于在图像中定位特定物体，如标志、图标等。
- 目标跟踪: 用于在视频中跟踪目标物体。
- 图像配准: 用于将两幅图像对齐。

模板匹配的实现步骤
1. 加载图像: 读取搜索图像和模板图像。

2. 模板匹配: 使用 cv2.matchTemplate() 在搜索图像中查找模板图像。

3. 获取匹配结果: 使用 cv2.minMaxLoc() 获取最佳匹配位置。

4. 绘制匹配结果: 在搜索图像中绘制匹配区域。

5. 显示结果: 显示匹配结果。

## matchTemplate()
``result = cv2.matchTemplate(image, templ, method, result=None, mask=None)``  
模板越小，计算量越小，但可能漏检；模板过大则易误匹配  
对光照敏感，建议预处理（如直方图均衡化）或使用归一化方法（如 TM_CCOEFF_NORMED）  
模板匹配对旋转和缩放不鲁棒，需结合其他算法（如 SIFT、ORB）或金字塔多尺度匹配  
多目标匹配：通过阈值化（np.where(result > threshold)）可检测多个匹配位置  
限制匹配区域（如 ROI）可以减少无效计算


```python
import cv2
import numpy as np

# 加载目标图像和模板图像
img = cv2.imread('target_image.jpg', 0)
template = cv2.imread('template_image.jpg', 0)

# 获取模板图像的尺寸
w, h = template.shape[::-1]

# 进行模板匹配
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

# 获取最佳匹配位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc  # 使用TM_CCOEFF_NORMED时取最大值位置，若使用 TM_SQDIFF 或 TM_SQDIFF_NORMED，最小值位置（min_loc）为最佳匹配

# 绘制矩形框标注匹配区域
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, top_left, bottom_right, 255, 2)

# 显示结果图像
cv2.imshow('Matched Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```


```python
import cv2
import numpy as np

# 加载目标图像和模板图像
img = cv2.imread('target_image.jpg', 0)
template = cv2.imread('template_image.jpg', 0)

# 获取模板图像的尺寸
w, h = template.shape[::-1]

# 进行模板匹配
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

# 设置匹配阈值
threshold = 0.8

# 找到匹配位置
loc = np.where(res >= threshold)

# 在目标图像中标记匹配位置
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

# 显示结果图像
cv2.imshow('Matched Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

# 图像拼接
图像拼接是计算机视觉中的一个重要应用，它可以将多张有重叠区域的图像拼接成一张更大的图像。  

应用场景  
全景图生成: 将多幅图像拼接成一幅全景图。  
地图拼接: 将多幅地图图像拼接成一幅更大的地图。  
医学图像处理: 将多幅医学图像拼接成一幅完整的图像。  

图像拼接的基本流程  
1. 图像读取：读取需要拼接的图像。

2. 特征点检测：在每张图像中检测出特征）。OpenCV 提供了多种特征点检测算法，如 SIFT、SURF、ORB 等

3. 特征点匹配：在不同图像之间匹配这些特征点。OpenCV 提供了 BFMatcher 或 FlannBasedMatcher 来进行特征点匹配

4. 计算变换矩阵：根据匹配的特征点计算图像之间的变换矩阵。

5. 图像融合：将图像按照变换矩阵进行拼接，并进行融合处理以消除拼接痕迹。


## SIFT_creat()
``sift = cv2.SIFT_create(nfeatures=0, nOctaveLayers=3, contrastThreshold=0.04, edgeThreshold=10, sigma=1.6)``  

nfeatures (可选)：保留的最佳特征数量（按对比度排序）。默认值 0 表示不限制数量，返回所有检测到的特征。

nOctaveLayers (可选)：每个金字塔组（Octave）中的层数。

contrastThreshold (可选)：过滤弱特征的对比度阈值。值越小，检测到的特征越多（包括低对比度区域）。

edgeThreshold (可选)：过滤边缘特征的阈值（避免检测到边缘响应而非角点）。值越大，保留的边缘特征越少。

sigma (可选)：高斯模糊的初始sigma值，用于构建尺度空间。

返回一个 cv2.SIFT 对象，可用于以下操作：

- 检测关键点：sift.detect(image)

- 计算描述符：sift.compute(image, keypoints)

- 同时检测和计算：sift.detectAndCompute(image, mask)


```python
import cv2
import numpy as np

# 1. 加载图像
image1 = cv2.imread(r"C:\Users\LENOVO\Pictures\Saved Pictures\1679907039016722.jpg")

# 2. 转换为灰度图
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# 3. 特征点检测
sift = cv2.SIFT_create()
keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
# detectAndCompute() 函数会返回两个值：关键点（keypoints）和描述符（descriptors）。
# 关键点是图像中的显著点，描述符是对这些关键点的描述，用于后续的匹配。

# 绘制关键点
output_image = cv2.drawKeypoints(image1, keypoints1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# 显示结果
cv2.imshow('SIFT Features', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## xfeatures2d.SURF_create()
SURF 是 SIFT 的加速版本，对尺度、旋转和光照变化具有较好的不变性，但受专利保护，需通过 opencv-contrib-python 安装  
>```python
>surf = cv2.xfeatures2d.SURF_create(
>    hessianThreshold=400,  # Hessian阈值，控制关键点数量（值越高，关键点越少）
>    nOctaves=4,           # 金字塔组数（默认4）
>    nOctaveLayers=3,      # 每组金字塔的层数（默认3）
>    extended=False,       # 是否使用扩展描述符（128维，默认64维）
>    upright=False         # 是否禁用旋转不变性（True=更快，False=更准确）
>)
>```

## ORB_create()
ORB 是一种快速、无专利限制的特征检测算法，适合实时应用（如 SLAM、AR），但对尺度变化敏感
>```python
>orb = cv2.ORB_create(
>    nfeatures=500,        # 保留的最佳特征数量（默认500）值越小速度越快但可能丢失重要特征
>    scaleFactor=1.2,      # 金字塔缩放因子（默认1.2）值越大金字塔层数越少，速度越快但对尺度变化更敏感
>    nlevels=8,            # 金字塔层数（默认8）
>    edgeThreshold=31,     # 边缘阈值（默认31）
>    firstLevel=0,         # 金字塔起始层（默认0）
>    WTA_K=2,             # BRIEF描述符的采样点数（2或3）
>    scoreType=cv2.ORB_HARRIS_SCORE,  # 关键点评分方式（HARRIS_SCORE或FAST_SCORE）
>    patchSize=31          # BRIEF描述符的补丁大小（默认31）
>)

## cv2.BFMatcher()
``matcher = cv2.BFMatcher(normType=cv2.NORM_L2,crossCheck=False)``

normType（距离度量方式）
- cv2.NORM_L1：曼哈顿距离（适用于 SIFT、SURF 的浮点型描述符）

- cv2.NORM_L2（默认）：欧氏距离（适用于 SIFT、SURF 的浮点型描述符）

- cv2.NORM_HAMMING：汉明距离（适用于 ORB、BRIEF、BRISK 的二进制描述符）

- cv2.NORM_HAMMING2：改进的汉明距离（适用于 ORB 的 WTA_K=3 或 4 的情况）

crossCheck（交叉验证）
- False（默认）：返回每个查询描述符的最近邻匹配（可能存在错误匹配）

- True：仅保留双向匹配一致的点对（更准确，但匹配数量减少）

``matcher.match(descriptors1, descriptors2)``  
功能：返回两组描述符之间的最佳匹配（每个查询描述符的最近邻）。  
返回值：DMatch 对象列表，每个 DMatch 包含：queryIdx：查询描述符的索引。trainIdx：训练描述符的索引。distance：匹配距离（值越小越匹配）。  

``matcher.knnMatch(descriptors1, descriptors2, k)``  
功能：返回每个查询描述符的前 k 个最近邻匹配（用于 RANSAC 等过滤错误匹配的算法）。  
返回值：列表的列表，每个子列表包含 k 个 DMatch 对象  


```python
import cv2
import numpy as np

# 1. 加载图像
image1 = cv2.imread("path/to/image1.jpg")
image2 = cv2.imread("path/to/image2.jpg")

# 2. 转换为灰度图
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# 3. 特征点检测
sift = cv2.SIFT_create()
keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

# 4. 特征点匹配
matcher = cv2.BFMatcher()
matches = matcher.knnMatch(descriptors1, descriptors2, k=2)

# 5. 应用比率测试，筛选匹配点
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# 6. 计算单应性矩阵
if len(good_matches) > 10:
    src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0) # findHomography() 函数会返回一个 3x3 的单应性矩阵 H，它可以将 image1 中的点映射到 image2 中
else:
    print("Not enough matches found.")
    exit()

# 7. 图像变换
height1, width1 = image1.shape[:2]
height2, width2 = image2.shape[:2]
warped_image = cv2.warpPerspective(image1, H, (width1 + width2, height1))

# 8. 图像拼接
warped_image[0:height2, 0:width2] = image2

# 9. 显示结果
cv2.imshow("Stitched Image", warped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

# 简单滤镜


```python
## 怀旧滤镜
import cv2
import numpy as np

# 读取图像
image = cv2.imread('input.jpg')

# 分离 BGR 通道
b, g, r = cv2.split(image)

# 调整通道强度  增加红色和绿色通道的强度，同时减少蓝色通道的强度
r = np.clip(r * 0.393 + g * 0.769 + b * 0.189, 0, 255).astype(np.uint8)
g = np.clip(r * 0.349 + g * 0.686 + b * 0.168, 0, 255).astype(np.uint8)
b = np.clip(r * 0.272 + g * 0.534 + b * 0.131, 0, 255).astype(np.uint8)

# 合并通道
vintage_image = cv2.merge((b, g, r))

# 保存怀旧图像
cv2.imwrite('vintage_output.jpg', vintage_image)

# 显示怀旧图像
cv2.imshow('Vintage Image', vintage_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```


```python
## 浮雕滤镜
import cv2
import numpy as np

# 读取图像
image = cv2.imread('input.jpg')

# 转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 定义卷积核
kernel = np.array([[-2, -1, 0],
                   [-1,  1, 1],
                   [ 0,  1, 2]])

# 应用卷积核
emboss_image = cv2.filter2D(gray_image, -1, kernel)

# 保存浮雕图像
cv2.imwrite('emboss_output.jpg', emboss_image)

# 显示浮雕图像
cv2.imshow('Emboss Image', emboss_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```


```python
## 锐化滤镜
import cv2
import numpy as np

# 读取图像
image = cv2.imread("path/to/image.jpg")

# 锐化滤镜
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
sharpened_image = cv2.filter2D(image, -1, sharpen_kernel)

# 显示结果
cv2.imshow("Sharpen Filter", sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

# cv2.Tracker
