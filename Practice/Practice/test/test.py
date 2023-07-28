import cv2
import numpy as np
import copy
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
from typing import List

img = cv2.imread("/Users/pcy/Desktop/works/python/Practice/Practice/test/040.jpg")  # 이미지 읽기
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR -> RGB 순서 변경
img = cv2.resize(img, (128, 128))  # 이미지 크기 조정
img_arr1 = np.array(img)  # 배열로 변환
print(img_arr1)
print("========================")

img = cv2.imread("/Users/pcy/Desktop/works/python/Practice/Practice/test/Encrypted_img.jpg")  # 이미지 읽기
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR -> RGB 순서 변경
img = cv2.resize(img, (128, 128))  # 이미지 크기 조정
img_arr2 = np.array(img)  # 배열로 변환
print(img_arr2)

if img_arr1.all() == img_arr2.all():
    print("True")