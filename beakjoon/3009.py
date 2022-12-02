#%%
xy = [[],[]]
for _ in range(3):
    x, y =map(int, input().split())
    if x in xy[0]:
        xy[0].remove(x)
    else:
        xy[0].append(x)
    if y in xy[1]:
        xy[1].remove(y)
    else:
        xy[1].append(y)
print(*sum(xy, []))
# %%
