# 159

a = int(input())
b = list(sorted(map(int, input().split()), reverse=True))
for i in range(a):
    print(b[i])