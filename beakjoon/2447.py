# 퍼온코드
#%%
n = int(input())

def starpoint(n):

    if n == 1:
        return '*'
    
    stars = starpoint(n//3)
    L = []

    for star in stars:
        L.append(star*3)
    for star in stars:
        L.append(star+" "*(n//3)+star)
    for star in stars:
        L.append(star*3)

    return L

print('\n'.join(starpoint(n)))
# %%

# %%
