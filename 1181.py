#%%
n = int(input())
words = set([input().strip() for _ in range(n)])

words = list(words)
words.sort()
words.sort(key= len)
for i in words:
    print(i)
# %%

'''
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours'''