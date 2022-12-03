canvas = [[0]*100 for _ in range(100)]
n = int(input())
for i in range(n):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            canvas[i][j] = 1

print(sum(sum(canvas,[])))