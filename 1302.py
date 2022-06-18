#%%
n = int(input())
books = []
best_seller=[]
max_num = 0
for i in range(n):
    books.append(input().lower())
for i in books:
    if i not in best_seller and max_num < books.count(i):
        best_seller=[]
        best_seller.append(i)
        max_num = books.count(i)

    elif i not in best_seller and max_num == books.count(i):
        best_seller.append(i)
        max_num = books.count(i)
print(sorted(best_seller)[0])
# %%

# %%
