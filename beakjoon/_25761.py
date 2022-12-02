# 시간초과뜨는 코드. 강해져서 다시 돌아오도록 하자.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
land = []

for i in range(n):
    line = str(input().strip()).replace('.', '0').replace('#', '1')
    land.append(list(map(int, line)))
    
q = int(input())
for _ in range(q):
    hope = list(map(int, input().split()))
    temp2 = 0
    
    for i in range(n-(hope[0]-1)):
        for j in range(m-(hope[1]-1)):
            
            if not sum(land[i][j:j+hope[1]]):
                temp = 0
                
                for k in range(i+1, i+hope[0]):
                    if sum(land[k][j:j+hope[1]]):
                        temp += 1
                        break
            else:
                temp = 1
                
            if not temp:
                temp2 += 1
                break
    if temp2:
        print('YES')
    else:
        print('NO')
        


