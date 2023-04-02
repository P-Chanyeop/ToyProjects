a = np.array(decrypted_img, order='F')  # Fortran-컨티규어스 배열 생성
decrypted_img = np.ascontiguousarray(a.T).copy()  # 전치 및 C-컨티규어스 형식으로 바꾸기