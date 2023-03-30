from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from PIL import Image
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import os
import cv2

def encrypt_image(input_file, key):
    # 이미지 파일을 열어서 바이트 형태로 읽어들입니다.
    with open(input_file, 'rb') as f:
        image_data = f.read()

    # DES 객체를 생성하고 암호화할 이미지 데이터를 패딩합니다.
    des = DES.new(key, DES.MODE_ECB)
    padded_image_data = pad(image_data, des.block_size)

    # 암호화된 이미지 데이터를 생성합니다.
    encrypted_image_data = des.encrypt(padded_image_data)

    return encrypted_image_data
    # # 암호화된 이미지를 파일로 저장합니다.
    # with open(output_file, 'wb') as f:
    #     f.write(encrypted_image_data)
        
# Function to Display Image
def imgdis(path): 
    img = mpimg.imread(path) 
    imgplot = plt.imshow(img)
    plt.show(imgplot)

def decrypt_image(input_file, key):
    # 암호화된 이미지 파일을 열어서 바이트 형태로 읽어들입니다.
    with open(input_file, 'rb') as f:
        encrypted_image_data = f.read()

    # DES 객체를 생성하고 복호화할 이미지 데이터를 패딩합니다.
    des = DES.new(key, DES.MODE_ECB)
    padded_image_data = des.decrypt(encrypted_image_data)

    # 패딩된 이미지 데이터를 언패딩합니다.
    image_data = unpad(padded_image_data, des.block_size)

    return image_data
    # # 복호화된 이미지를 파일로 저장합니다.
    # with open(output_file, 'wb') as f:
    #     f.write(image_data)


# input_file = '040.jpg'
# output_file = 'images/040.jpg'
# key = os.urandom(8)
# print(f'암호화 키 : {key}')

# encrypt_image(input_file, output_file, key)

# input_file2 = 'images/040.jpg'
# output_file2 = '041.jpg'
# key2 = b'@\x9f\xfa0\xd5\x90\x03\xbd'
# decrypt_image(input_file2, output_file2, key2)


image = cv2.imread("images/040.jpg", cv2.IMREAD_UNCHANGED)
height, width, channel = image.shape
print(height, width , channel)
cv2.imshow("crypto image", image)
cv2.waitKey()
cv2.destroyAllWindows()