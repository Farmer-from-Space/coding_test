#561

a =  list(map(int, input().split()))
b = []
c = []
for i in a:
    if 1 <= i < 100:
        b.append(i)
    elif 10000 > i >= 100:
        c.append(i)
if b==[]:
    b.append(100)
if c==[]:
    c.append(100)
print(max(b), min(c))