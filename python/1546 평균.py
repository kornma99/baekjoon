a=int(input())

list1=list(map(int,input().split(" ")))

list1.sort()

b = list1[-1]
c=0
for i in range(len(list1)):
    c += list1[i]/b*100

print(c/a)
