n = int(input())
ns = sorted([ int(input()) for _ in range(n)])

for i in range(2, ns[0]):
    ns_len = n-1
    
    for j in range(n):
        if j == 0:
            r = ns[j]%i
        elif r == ns[j]%i:
            ns_len -= 1
    if ns_len == 0:
        print(i, end = ' ')
        