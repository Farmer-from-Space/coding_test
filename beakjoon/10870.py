#%%
n =  int(input())

def fivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(fivo(n-1) + fivo(n-2))

print(fivo(n))
# %%

n =  int(input())
r = []
for i in range(n+1):
    if i >= 2:
        i = r[i-1]+ r[i-2]
    r.append(i)
print(r[-1])
# %%
