n = int(input())

p = [0,1,2] + [0]*(n-2)
for i in range(3, n+1):
    p[i] = (p[i-1] + p[i-2]) %15746

print(p[n])