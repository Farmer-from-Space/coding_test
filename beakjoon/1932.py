import sys
input = sys.stdin.readline

n = int(input())

dp = [[int(input())]]

for i in range(n-1):
    temp = list(map(int, input().split()))
    for j in range(i+2):
        if j == 0:
            temp[j] += dp[-1][j]
        elif j == i+1:
            temp[j] += dp[-1][j-1]
        else:
            temp[j] += max(dp[-1][j], dp[-1][j-1])
    dp.append(temp)
print(max(dp[-1]))