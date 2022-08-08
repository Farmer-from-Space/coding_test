#%%
import sys
input = sys.stdin.readline
n = int(input())

for i in range(n+1):
    i2 = i
    for j in str(i):
        i2 += int(j)
    if i2 == n:
        print(i)
        break
    if i == n:
        print(0)
# %%
import sys
input = sys.stdin.readline
n = int(input())
for i in range(n+1):
    data = list(map(int, str(i)))
    r = i+sum(data)
    if r == n:
        print(i)
        break
    if i == n:
        print(0)
# %%
