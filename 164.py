# 실제 채점 과정이 안내된 문제와 다름.
#%%
for i in range(4):
    a =  list(map(int, input().split()))
    print(f'{i+1}class : {sum(a)}')
# %%

# for i in range(4):
#     a =  list(map(int, input().split()))
#     name =  a[0][:-1]
#     num = map(int, a[1:])
#     print(f'{i+1}class : {sum(num)}')