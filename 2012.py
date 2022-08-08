#%%
n = int(input())
s = [int(input()) for _ in range(n)]
s.sort()
for i, n in enumerate(s):
    s[i] = abs(i+1-n)

print(sum(s))



# %%
