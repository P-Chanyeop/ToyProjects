# 화씨온도 변환기
# 화씨온도(F) = (섭씨온도(C) * 1.8) + 32

print("섭씨온도를 화씨온도로 변환하는 프로그램입니다.")
print("변환하고자 하는 섭씨온도를 입력하세요 >> ", end="")
celsius = input()
fahrenheit = (float(celsius) * 1.8) + 32

print("섭씨온도 : ", celsius)
print("화씨온도 : ", fahrenheit)
30