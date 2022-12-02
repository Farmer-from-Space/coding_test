a = list(map(int, input().split()))
a.append(100)
a= sorted(a, reverse = True)

while a[-1] >= 0:
  a.append(a[-2]-a[-1])
print(*a, sep =" ") 