#%%
total = list(i for i in range(3000000) if '666' in str(i))
n = int(input())
print(total[n-1])
# %%
n = int(input())
total = []
i = 666
while len(total) < n:
    if '666' in str(i):
        total.append(i)
    i += 1

print(total[n-1])
# %%
