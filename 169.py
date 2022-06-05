#%%
strs = []
for _ in range(3):
    a = list(map(str, input().split()))
    a =  [x.lower() for x in a]
    strs.append(a)

for i in range(len(strs)):
    print(*strs[i], sep=" ")
# %%
