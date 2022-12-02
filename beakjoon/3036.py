n = int(input())
nums = list(map(int, input().split()))

for i in range(1, n):
    a, b = nums[0], nums[i]
    c = b
    r = a%b
    while r != 0:
        c, r = r, c%r
    print(f'{a//c}/{b//c}')
    