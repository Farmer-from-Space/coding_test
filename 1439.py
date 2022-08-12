#%%
n = input()
count = 0
for i in range(len(n)-1):
    if n[i] != n[i+1]:
        count+=1
if count%2:
    answer = count//2 + 1
else:
    answer = count//2
print(answer)
# %%
n = input()
count = 0
for i in range(len(n)):
    if n[i] != n[i-1]:
        count+=1

print(count//2)
# %%
