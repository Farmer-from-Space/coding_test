#%%
# dic으로 풀이
n, m= map(int, input().split())
s = {}
count = 0
for _ in range(n):
    s[input()] = 1
for _ in range(m):
    count += s.get(input(), 0)
print(count)
# %%
# set에서는 in으로 탐색하는게 list랑 달리 시간초과가 안뜬다
n, m= map(int, input().split())
s = set([input() for i in range(n)])
count = 0
for _ in range(m): 
    if input() in s:
        count += 1
print(count)

#%%

'''
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink'''
# %%
