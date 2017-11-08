from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.144])


img = np.array(Image.open('d:/5041.png'))  # 打开图像并转化为数字矩阵

rows, cols, point = img.shape
for i in range(rows):
    for j in range(cols):
        img[i, j] = rgb2gray(img[i, j])

plt.figure("lena")
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()
