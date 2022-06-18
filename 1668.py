#%%
n = int(input())
height = []
left = 0
right = 0

for i in range(n):
    height.append(int(input()))

max = 0
for i in range(len(height)):
    if max < height[i]:
        max = height[i]
        left +=1

height.reverse()

max = 0
for i in range(len(height)):
    if max < height[i]:
        max = height[i]
        right +=1
print(left)
print(right)
# %%
