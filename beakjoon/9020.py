#%%
# import sys
# input = sys.stdin.readline

t = int(input())
n = [int(input()) for _ in range(t)]

ss_range= set([i for i in range(2, max(n)+1) if i%2 or i ==2])
d =  int(max(n)**.5) +1

for i in range(3, d, 2): 
    ss_range -= set(range(i*2, max(n)+1, i))

ss_range =  sorted(list(ss_range))
for j in n:
    for h in range(j//2, 1, -1):
        if h in ss_range and j - h in ss_range:
            print(h, j-h)
            break
# %%

#퍼온코드

import sys
import math

x = 10001
nums = [True]*x
nums[0]=False; nums[1]=False
limit = int(math.sqrt(x))+1
for i in range(2, limit):
    if nums[i]:
        for j in range(i+i, x, i):
            nums[j]=False

n = int(sys.stdin.readline())
for _ in range(n):
    tmp = int(sys.stdin.readline())
    for i in range(tmp//2, 1, -1):
        if nums[i] and nums[tmp-i]:
            print(i, tmp-i, sep=' ')
            break

#%%
# 퍼온코드+ 조합

x = 10001
nums = [False, False]+[True]*(x-1)

for i in range(int(x**.5) + 1):
    if nums[i]: 
        nums[2*i::i] = [False]*(x//i - 1) 

n = int(input())
for _ in range(n):
    tmp = int(input())
    for i in range(tmp//2, 1, -1):
        if nums[i] and nums[tmp-i]:
            print(i, tmp-i, sep=' ')
            break
# %%
