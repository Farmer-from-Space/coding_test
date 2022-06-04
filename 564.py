a = list(map(str, input().split()))
b = []
a = sorted(a)
for i in a:
  if i != "!" and i not in b and i.isupper():
    print(f"{i} : {a.count(i)}")
    b.append(i)