n, m = map(int, input().split())
nums = []
def pp():
    if len(nums) == m:
        print(*nums, sep=' ')
        return
    
    for i in range(1,n+1):
        nums.append(i)
        pp()
        nums.pop()
pp()