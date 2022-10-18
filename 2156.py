n = int(input())
wines = [ int(input()) for _ in range(n)]
dp = [0] * n

if n == 1:
    print(wines[0])
elif n == 2:
    print(wines[1]+wines[0])
else:
    dp[0], dp[1] = wines[0], wines[1]+wines[0]
    for i in range(2,n):
        dp[i] = max(dp[i-1], wines[i]+dp[i-2], wines[i]+wines[i-1]+dp[i-3])

    print(dp[-1])