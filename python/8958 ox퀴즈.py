a=int(input())
ox=[]
for i in range(a):
    ox.append(input())
print(ox)

for i in range(len(ox)):
    sum=0
    score=0
    for r in range(len(ox[i])):
        if ox[i][r] == "O":
            sum += 1
            score += sum
        else:
            sum=0
    print(score)