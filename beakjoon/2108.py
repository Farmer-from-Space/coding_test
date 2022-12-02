#%%
import sys
from collections import Counter
input = sys.stdin.readline
n=int(input())
nums = sorted([int(input()) for _ in range(n)])

print(round(sum(nums)/n))
print(nums[n//2])
if len(nums) == 1:
    print(nums[0])
elif Counter(nums).most_common(2)[0][1] == Counter(nums).most_common(2)[1][1]:
    print(Counter(nums).most_common(2)[1][0])
else:
    print(Counter(nums).most_common(2)[0][0])
print(nums[-1]-nums[0])

# %%