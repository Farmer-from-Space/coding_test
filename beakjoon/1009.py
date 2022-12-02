#%%
import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    c =a
    for _ in range(b%4+3):
        c = int(str(c * a)[-1])
    
    if c == 0:
        print(10)
    else:
        print(c)
# %%
# %%
100%4

# %%
