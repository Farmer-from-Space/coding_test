#%%
for i in range(2):
    name = input()
    temp = []
    for j in range(2):
        temp.append(list(map(int, input().split())))
    if i == 1:
        break
    nums1 = temp
nums2 = temp
for i in range(len(nums1)):
    result =[]
    for j in range(len(nums1[i])):
        result.append(nums1[i][j]*nums2[i][j])
    print(*result, sep=" ")
# %%
