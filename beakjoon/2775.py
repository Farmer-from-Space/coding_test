#%%
T =  int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    
    l = [[i for i in range(1,15)]]
    for i in range(1, k+1):
        h = [sum(l[i-1][:j]) for j in range(1,15)]
        l.append(h)
    print(l[k][n-1])
        
# %%
