n ,m = map(int, input().split())
castle = []
count = 0
count2 = 0
for i in range(n):
    castle.append(input())

for i in range(n):
    if 'X' not in castle[i]:
        count += 1
for j in range(m):
    temp = 0
    for i in range(n):
        if castle[i][j] != 'X':
            temp +=1
    if temp == n :
        count2 += 1
if count2 > count:
    count =  count2
print(count)
