#153

x=[]
a =  list(map(int, input().split()))
for i in a:
    if i != -1:
        x.append(i)

print(*x[-3:], sep= " ")