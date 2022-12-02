#158

a =  list(map(int, input().split()))
a = a[:-1]
b=[]
for i in a:
    if i%2==0:
        b.append(i//2)
    else:
        b.append(i*2)
        
print(len(b))
print(*b, sep=" ")