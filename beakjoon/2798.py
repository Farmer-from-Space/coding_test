from itertools import combinations


#%%
from itertools import combinations
n, m = map(int, input().split())
cards = list(map(int, input().split()))
sums = []
for i in combinations(cards, 3):
    if sum(i) <= m:
        sums.append(sum(i))
print(max(sums))    

# %%
