import sys
input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(3):
        costs[i][j] += min([costs[i-1][k] for k in range(3) if k != j])
print(min(costs[-1]))

    