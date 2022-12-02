import sys
input = sys.stdin.readline
n = int(input())
pn = [0] + [1] * 100
for i in range(4, 101):
    pn[i] = pn[i-2] + pn[i-3]

for _ in range(n):
    print(pn[int(input())])