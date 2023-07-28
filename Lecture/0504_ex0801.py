ss = '파이썬은완전재미있어요'

sslen = len(ss)

for i in range(sslen):
    if(i % 2 == 1):
        print('#', end='')
    else:
        print(ss[i], end='')