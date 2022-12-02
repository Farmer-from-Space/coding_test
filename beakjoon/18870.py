#%%
n= int(input())
xs = list(map(int, input().split()))
xs2 = sorted(set(xs))

dic = { xs2[i]:i for i in range(len(xs2))}

for j in xs:
    print(dic[j], end=' ')

# for j in range(len(xs)):
#     xs[j] = dic[xs[j]]
# print(*xs, sep=' ')
# %%
