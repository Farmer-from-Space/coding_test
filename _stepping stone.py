# 6:25
#%%
from itertools import combinations
def solution(distance, rocks, n):
    
    combi = []
    min_lens = []
    # 바위 n개를 뺀 rocks의 조합을 구함
    for i in combinations(rocks, len(rocks)-n):
        i = list(i)
        i.append(0)
        i.append(distance)
        combi.append(sorted(i))
    
    # 거리의 최소값을 구함
    for i in combi:
        lens = []
        for j in range(len(i)):
            if j != 0:
                lens.append(i[j]-i[j-1])
        min_lens.append(min(lens))
    
    # 그중 가장 큰 값을 구함    
    return max(min_lens)

#%%
solution(25, [2, 14, 11, 21, 17], 2)
# %%
import heapq
def solution(distance, rocks, n):
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    
    # 기존 최소값을 가진 바위를 n번 제거해가면서 최소값을 최대화
    while n >= 0:
        lens = []
        for j in range(len(rocks)):
            if j != 0:
              heapq.heappush(lens, (rocks[j]-rocks[j-1], rocks[j]))
        if n == 0:
            break
        rocks.remove(heapq.heappop(lens)[1])
        
        n -= 1
        
        
    # 새로운 간격중 최소값
    return heapq.heappop(lens)[0]

#%%
solution(25, [2, 14, 11, 21, 17], 2)

# %%
 [0, 2, 11, 14, 17, 21, 25]
  2   9    3   3   4   4