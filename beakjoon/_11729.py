#%%
n = int(input())
a,b,c =list(range(n, 0, -1)),[],[]
process = []
while len(c) != n:
    if (a and not c) or a[-1] < c[-1]:
        c.append(a.pop())
        process.append("1 3")
        
    if (a and not b) or a[-1] < b[-1]:
        b.append(a.pop())
        process.append("1 2")
    
# %%
a = list(range(5))
# %%
print(a)
# %%
def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    hanoi_tower(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi_tower(n-1, 6-start-end, end) # 3단계
    
n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)
# %%