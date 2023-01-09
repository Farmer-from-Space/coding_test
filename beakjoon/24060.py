total_arr = []
def merge_sort(nums, total_arr):
    if len(nums) < 2:
        return nums, total_arr

    # 문제에서 리스트가 홀수일때 00 000 이런 상태가 아닌 000 00로 되는걸 맞추기 위함
    if len(nums) % 2:
        mid = len(nums) // 2 + 1
    else:
        mid = len(nums) // 2

    low, total_arr = merge_sort(nums[:mid], total_arr)
    high, total_arr = merge_sort(nums[mid:], total_arr)
    
    l = r = 0
    new_arr = []
    while l < len(low) and r < len(high):
        if low[l] < high[r]:
            new_arr.append(low[l])
            total_arr.append(low[l])
            l += 1
        else:
            new_arr.append(high[r])
            total_arr.append(high[r])
            r += 1
            
    for i in low[l:]:
        new_arr.append(i)
        total_arr.append(i)
    
    for i in high[r:]:
        new_arr.append(i)
        total_arr.append(i)
    
    return new_arr, total_arr

_, k = map(int, input().split())
nums = list(map(int, input().split()))

nums, total_arr = merge_sort(nums, total_arr)

if len(total_arr) < k:
    print(-1)
else:
    print(total_arr[k-1])
