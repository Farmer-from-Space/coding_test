#%%
n = sorted(list(map(int, input().split())))
while sum(n) != 0:

    if n[2]**2 == n[0]**2 + n[1]**2:
        print('right')
    else:
        print('wrong')

    n = sorted(list(map(int, input().split())))
# %%