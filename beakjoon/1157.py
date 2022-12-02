#%%
word = input().upper()
l = {}
for i in word:
    if i not in l:
        l[i] = 1
    else:
        l[i] += 1

l =  sorted(l.items(), key = lambda x:x[1], reverse=True)

if len(l) > 1 and l[0][1] == l[1][1]:
    print('?')
else:
    print(l[0][0])

# %%
