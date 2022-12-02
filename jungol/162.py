#%%
a = list(map(int, input().split()))
while len(a) < 10:
    a.append(int(str(a[-1]+a[-2])[-1]))
print(*a, sep=" ")
# %%
