#%%
m, n = map(int, input().split())
r =  set(range(m, n+1))
r -= {1}
y = int(n**0.5) +1
for i in range(2, y):
    r -= set(range(i*2, n+1, i))
    
r = sorted(list(r))
for i in r:
    print(i)
# %%
