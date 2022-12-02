#%%
n = int(input())
mins = list(map(int, input().split()))
mins.sort()
a = 0

for i in range(len(mins)):
    a += sum(mins[:i+1])

print(a)

# %%
