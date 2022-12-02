# 558
x=[]
a =  list(map(int, input().split()))
for i in a:
    if i != 0:
        x.append(i)
x.reverse()
print(*x, sep= " ")