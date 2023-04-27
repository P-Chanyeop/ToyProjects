# 코드 07-04를 aa 리스트에 3의 배수 200개를 입력받도록 수정. 
# 리스트 bb는 리스트 aa의 역순으로 저장되게끔 수정.

aa = []
bb = []
value = 0

for i in range(0, 200):
    aa.append(value)
    value += 3

# 리스트 a를 deep copy 한 후, reverse()함수로 역정렬
bb = aa.copy()
bb.reverse()
# print(bb[0:])
        
aa = [1,2,3]; aa = []; print(aa)
aa = [1,2,3]; aa = None; print(aa)
aa = [1,2,3]; del(aa); print(aa)