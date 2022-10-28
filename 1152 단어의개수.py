list1=input().split(" ")

for i in list1:
    if i == '':
        list1.remove(i)
for i in list1:
    if i.isalpha() == False :
        list1.remove(i)
print(len(list1))