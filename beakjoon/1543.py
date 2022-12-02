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

docu = str(input())
word = str(input())
count, start = 0, 0
while start <= len(docu)-len(word):
    if docu[start:start+len(word)] == word:
        count += 1
        start += len(word)
    else:
        start += 1
print(count)