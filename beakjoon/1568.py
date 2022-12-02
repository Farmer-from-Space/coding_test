#%%
n = int(input())
song = 1
sec = 0
while n > 0:
    n -= song
    song += 1
    sec += 1
    if n < song:
        song = 1
print(sec)
# %%