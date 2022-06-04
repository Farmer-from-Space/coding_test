#%%
a = [[1,1,1,1,1]]

for i in range(5):
    temp = [1]
    if i > 0:
        for j in range(5):
            if j > 0:
                temp_num = a[i-1][j] + temp[j-1]
                temp.append(temp_num)
        a.append(temp)

for i in a:
    print(*i, sep=" ")