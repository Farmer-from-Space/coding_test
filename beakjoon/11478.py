#%%
# from itertools import permutations

s = input()
ss = []
i = 1
while i <= len(s):
    for j in range(i):
        ss.append(s[j:j+len(s)-i+1])
    i += 1
print(len(set(ss)))
# %%
