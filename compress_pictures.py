# 缩放图像

import numpy as np 
import cv2
from os.path import dirname, join, basename
from glob import glob

num = 0
for i in glob(r'C:\Users\Dell\Desktop\my_pig_original\*.jpg'):   # glob()获取指定目录下的所有文件
    img = cv2.imread(i)
    '''
    interpolation 即插值法
    INTER_AREA  - 使用像素区域关系进行重采样。
    它可能是图像抽取的首选方法，因为它会产生无云纹理的结果。
    但是当图像缩放时，它类似于INTER_NEAREST方法
    '''
    res = cv2.resize(img, (194, 259), interpolation=cv2.INTER_AREA)
    cv2.imwrite('C:\\Users\\Dell\\Desktop\\my_pig\\' + str(num) + '.jpg', res)
    num += 1
print('all done')

# 窗口默认一直处于弹出窗状态
cv2.waitKey(0)
# 按任意键盘，销毁窗口
cv2.destroyAllWindows()

