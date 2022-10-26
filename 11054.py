n = int(input())
nums = list(map(int, input().split()))
nums_re = nums[::-1]
dp = [1]*n
dp_re = [1]*n
for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] <= dp[j]:
            dp[i] = dp[j]+1            
        if nums_re[i] > nums_re[j] and dp_re[i] <= dp_re[j]:
            dp_re[i] = dp_re[j]+1
dp_re = dp_re[::-1]
for i in range(n):
    dp[i] = dp[i] + dp_re[i] - 1

print(max(dp))
