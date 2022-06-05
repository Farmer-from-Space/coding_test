#%%
h = int(input())
pascal =[]
for i in range(h):
    temp=[]
    for j in range(i+1):
        if j == 0 or j == i:
            temp.append(1)
        else:
            temp.append(pascal[i-1][j-1]+pascal[i-1][j])
    pascal.append(temp)

for i in pascal[::-1]:
    print(*i, sep =" ")
# %%
