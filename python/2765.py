a = int(input())
list1=[]
for i in range(a):
    list1.append(input().split(" "))
list2=[]
for i in range(len(list1)):
    for r in range(len(list1[i])):
        list2.append(list1[i][r])

for i in range(a):
    for r in range(len(list2[2*(i+1)-1])):
        print(int(list2[2*i])*list2[2*(i+1)-1][r], end="")
    print()