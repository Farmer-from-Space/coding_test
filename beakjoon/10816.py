#%%
n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

sanggeun_cards = {}

for i in range(n):
    if ns[i] in sanggeun_cards:
        sanggeun_cards[ns[i]] += 1
    else:
        sanggeun_cards[ns[i]] = 1
for j in range(m):
    print(sanggeun_cards.get(ms[j], 0), end=' ')
# %%