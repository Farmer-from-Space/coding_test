a = list(map(int, input().split()))
b = []
c = []
for i in a:
  if i != 0:
    b.append(int((f"{i:02}")[0]))
b = sorted(b)

for i in b:
  if i not in c:
    print(f'{i} : {b.count(i)}')
    c.append(i)