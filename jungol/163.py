#%%
a = [[3,5,9], [2,11,5],[8,30,10],[22,5,1]]
b = []
for i in a:
    print(*i, sep = " ")
    b += i
print(sum(b))
# %%
