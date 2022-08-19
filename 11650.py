#%%
n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
nums = sorted(nums, key= lambda x: (x[1], x[0]))
for i in nums:
    print(*i)
# %%
