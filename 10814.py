#%%
n = int(input())
p = []
for _ in range(n):
    x, y = map(str,input().split())
    p.append([int(x),y])
p.sort(key = lambda x: x[0])

for i in p:
    print(*i)
# %%
