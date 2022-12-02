# 4:11 ~ 4:25 (first try)~4:59(최종 48분)
# first채점 결과 정확성: 52.4  효율성: 23.8  합계: 76.2 / 100.0
# 모든음식의 지수를 K이상으로 만들수 없는 경우를 찾는데서 오래걸림.
#%%
import heapq

def solution(scoville, K):
    
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break
        first = heapq.heappop(scoville)    
        second = heapq.heappop(scoville)    
        new_food= first +(second*2)
        heapq.heappush(scoville, new_food)
        answer += 1
    
    return answer

#%%

solution([1, 2, 3, 9, 10, 12], 7)
#%%

