# loop Example 

# using while
i = 0
while i < 3:
    print('hello world')
    i = i + 1

j = 0
while j < 3:
    print("print('hello world " + str(j * 9) + "')")
    j = j + 1

# using while with condition
k = 0
while k < 5:
    if k == 4:{
        print(k)
    }
    k = k + 1

# using for 
test_list = ['one', 'two', 'three']
for name in test_list:
    print(name)

# advanced about for 
test_list2 = [0,1,2,3,4]
for item in test_list2:
    print(item)

for item in range(len(test_list2)):     # 자바의 for(int i = 0; i < test_list.length; i++) 과 같다.
    print(item)