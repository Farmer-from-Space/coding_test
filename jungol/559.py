# 559

score =[85.6, 79.5, 83.1, 80.0, 78.2, 75.0]

classroom =  list(map(int, input().split()))
total = 0
for i in classroom:
    total += score[i-1]
print(round(total, 1))