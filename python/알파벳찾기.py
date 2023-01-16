a = "abcdefghijklmnopqrstuvwxyz"
nomodic={}
for i in range(1,len(a)+1):
    nomodic[a[i-1]]=-1

shit=input()

for i in range(len(shit)):
    if shit[i] not in nomodic:
        pass
    elif nomodic[shit[i]] == -1:
        nomodic[shit[i]] = i
    
list2=nomodic.values()
strr=' '.join(str(s) for s in list2)
print(strr)