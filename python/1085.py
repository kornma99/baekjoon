list1=list(map(int,input().split(" ")))

a = abs(list1[0]-list1[2])
b = abs(list1[1]-list1[3])
c = list1[0]
d = list1[1]

list2=[a,b,c,d]

print(min(list2))