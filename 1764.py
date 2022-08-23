import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = sorted([input().strip() for _ in range(n)])
n_list = { i:0 for i in n_list }

for _ in range(m):
    word = input().strip()
    if word in n_list:
        n_list[word] += 1
print(sum(n_list.values()))
for k,v in n_list.items():
    if v:
        print(k)