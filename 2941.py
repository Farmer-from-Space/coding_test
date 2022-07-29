# 첫번째 방법으로 생각없이 풀었다가, 두번째로 다시 품. 솔직히 다른거 참고했는데, 쉬운문제인데 생각없이 푼거 반성함.
#%%
word = str(input())
counts = 0

if 'c=' in word:
    counts += word.count('c=')
    word = word.replace('c=',' ')
if 'c-' in word:
    counts += word.count('c-')
    word = word.replace('c-',' ')
if 'dz=' in word:
    counts += word.count('dz=')
    word = word.replace('dz=',' ')
if 'd-' in word:
    counts += word.count('d-')
    word = word.replace('d-',' ')
if 'lj' in word:
    counts += word.count('lj')
    word = word.replace('lj',' ')
if 'nj' in word:
    counts += word.count('nj')
    word = word.replace('nj',' ')
if 's=' in word:
    counts += word.count('s=')
    word = word.replace('s=',' ')
if 'z=' in word:
    counts += word.count('z=')
    word = word.replace('z=',' ')
word = word.replace(' ','')

counts += len(word)

print(counts)
# %%

word = str(input())
counts = 0
cro = ['c=', 'c-', 'dz=', 'dz=', 'd-', 'lj', 'nj', 's=','z=' ]
for i in cro:
    if i in word:
        word = word.replace(i, " ")
print(len(word))
# %%
