n = int(input())
lines = sorted([list(map(int, input().split())) for _ in range(n)])
lines_re = lines[::-1]
dp = [1]*n
dp_re = [0]*n
for i in range(1, n):
    for j in range(i):
        if lines[i][1] > lines[j][1] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1 
print(n-max(dp))
            