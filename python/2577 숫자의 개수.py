list1=[]
for i in range(3):
    list1.append(int(input()))

a = list1[0]*list1[1]*list1[2]

lista=list(str(a))

for i in ['0','1','2','3','4','5','6','7','8','9']:
    print(lista.count(i))