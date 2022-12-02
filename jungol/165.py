#%%
a = [[1,0,1,0,1]]
for i in range(4):
    b = []
    for j in range(len(a[0])):
        if j == 0:
            b.append(a[i][j+1])
        elif j == 4:        
            b.append(a[i][j-1])
        else:
            b.append(a[i][j-1]+a[i][j+1])
    a.append(b)
for i in a:
    print(*i, sep=" ")
# %%
