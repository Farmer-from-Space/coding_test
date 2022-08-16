#%%
n = int(input())
entire = []
for _ in range(n):
    x, y = map(int, input().split())
    entire.append([x,y])
grades = []
for i in entire:
    grade = 1
    for j in entire:
        if i != j and i[0] < j[0] and i[1] < j[1]:
            grade += 1
    grades.append(grade)
print(*grades, sep=" ")
# %%
