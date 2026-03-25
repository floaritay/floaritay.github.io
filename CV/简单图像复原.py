import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
image=cv2.imread(r'')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# 通过颜色阈值生成掩膜（修复黑色区域）
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_black = np.array([0, 0, 0])
upper_black = np.array([30, 255, 10]) #V值越小越暗
mask = cv2.inRange(image_hsv, lower_black, upper_black)

# 图像修复
inpainted_telea = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
inpainted_ns = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_NS)
 
# 显示结果
plt.figure(figsize=(12,5))

plt.subplot(1,4,1)
plt.imshow(image)
plt.title('image')
plt.axis('off')

plt.subplot(1,4,2)
plt.imshow(mask)
plt.title('mask')
plt.axis('off')

plt.subplot(1,4,3)
plt.imshow(inpainted_telea)
plt.title('Inpainted (TELEA)')
plt.axis('off')

plt.subplot(1,4,4)
plt.imshow(inpainted_ns)
plt.title('Inpainted (NS)')
plt.axis('off')

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

