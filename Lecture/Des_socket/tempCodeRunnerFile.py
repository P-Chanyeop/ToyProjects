img = cv2.imread("/Users/pcy/Desktop/works/python/Practice/040.jpg")  # 이미지 읽기
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR -> RGB 순서 변경
img = cv2.resize(img, (3840, 2160))  # 이미지 크기 조정

# plt.imshow(img)
# plt.show()

img_arr = np.array(img)  # 배열로 변환

ECB_encrypted_img = DES_ECB(img_arr, [1,2,3,4,5,6,7,8], round=16)
CBC_encrypted_img = DES_CBC(img_arr, [1,2,3,4,5,6,7,8], round=16)
OFB_encrypted_img = DES_OFB(img_arr, [1,2,3,4,5,6,7,8], round=16)

CBC_decrypted_img = DES_CBC_decrypt(CBC_encrypted_img, [1,2,3,4,5,6,7,8], round=16)

# ================== 암호화 이미지 =======================

plt.imshow(img)
plt.show()
plt.imshow(ECB_encrypted_img)
plt.show()
plt.imshow(CBC_encrypted_img)
plt.show()
plt.imshow(OFB_encrypted_img)
plt.show()

# ================== 복호화 이미지 =======================

plt.imshow(CBC_decrypted_img)