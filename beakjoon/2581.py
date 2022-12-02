# %%
m = int(input())
n = int(input())
ss = set(range(m, n+1))
ss -= {1}

checkn = int(n**0.5)+1
for j in range(2, checkn):
    ss -= set(range(j*2, n+1, j))

if ss:
    print(sum(ss))
    print(min(list(ss)))
else:
    print(-1)

# %%
