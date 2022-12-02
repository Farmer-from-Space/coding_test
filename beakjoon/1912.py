n = int(input())
nums = [0] + list(map(int, input().split()))
sums = [-1001]*(n+1)

for i in range(1, n+1):
    sums[i]= max(nums[i], nums[i]+sums[i-1])

print(max(sums))