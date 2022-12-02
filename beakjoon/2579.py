n = int(input())
steps = [0] + [int(input()) for _ in range(n)]
sums = [0] * (n+1)
if n == 1:
    print(sum(steps))
elif n ==2:
    print(sum(steps))
else:
    sums[1], sums[2] = steps[1], steps[1]+steps[2]
    for i in range(3, n+1):
        sums[i] = max(steps[i]+sums[i-2], steps[i]+steps[i-1]+sums[i-3])
    print(sums[-1])