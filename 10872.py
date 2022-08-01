#%%
n= int(input())
r = 1
for i in range(1, n+1):
    r *= i

print(r)
# %%

n = int(input())

def factorial(n):
    if n < 1:
        return 1
    else:
        return(n * factorial(n-1))
factorial(n)
# %%
