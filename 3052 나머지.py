list1=[]

for i in range(10):
    list1.append(int(input()))

for i in range(len(list1)):
    list1[i] = list1[i] % 42

list2=list(set(list1))
print(len(list2))
