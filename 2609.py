a,b = map(int, input().split())

for i in range(a, 0, -1):
    if not a%i and not b%i:
        print(i)
        break

for i in range(1, b+1):
    if not (a*i)%b :
        print(a*i)
        break