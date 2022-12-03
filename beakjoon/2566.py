maxnum = 0
maxindex = [0, 0]
for i in range(9):
    temp = list(map(int, input().split()))
    if maxnum <= max(temp):
        maxnum = max(temp)
        maxindex = [i+1, temp.index(max(temp))+1]

print(maxnum)
print(*maxindex)