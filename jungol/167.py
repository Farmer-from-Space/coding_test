#%%
b =[]
g_mean =[]
temp0 = []
temp1 = []

for _ in range(4):
    a = list(map(int, input().split()))
    b.append(a)
for i in b:
    g_mean.append(int(sum(i)/len(i)))
    temp0.append(i[0])
    temp1.append(i[1])

s_mean =[int(sum(temp0)/len(temp0)),int(sum(temp1)/len(temp1))]


print(*g_mean, sep=" ")
print(*s_mean, sep=" ")
print(int(sum(sum(b,[]))/len(sum(b,[]))))

# %%
