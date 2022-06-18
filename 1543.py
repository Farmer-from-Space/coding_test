#%%
docu = str(input())
word = str(input())
count = 0
i = 0
while word in docu:
    if docu[i:i+len(word)] == word:
        docu = docu[i+len(word):]
        count += 1
        i = 0
    else:
        i += 1
print(count)
# %%