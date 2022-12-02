#%%
a =  sorted(list(map(int, input().split())), reverse=True)
b = []
c = []
for i in a:
    if i != 0:
        b.append(str(i)[:-1]+'0')
for i in b:
    if i not in c:
        print(f'{i} : {b.count(i)} person')
        c.append(i)
# %%
