n, m = map(int, input().split())
nums = []
def pp(start):
    if len(nums) == m:
        print(*nums, sep=' ')
        return
    
    for i in range(start,n+1):
        if i not in nums:
            nums.append(i)
            pp(i+1)
        nums.pop()
pp(1)