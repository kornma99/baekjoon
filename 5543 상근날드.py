list1=[]
list2=[]
for i in range(3):
    list1.append(int(input()))

for i in range(2):
    list2.append(int(input()))

price=[]
for i in range(3):
    for r in range(2):
        price.append(list1[i]+list2[r]-50)

price.sort()
print(price[0])

# min과 max를 사용했다면 더 편했을거같다.
