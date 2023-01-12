#효율성 테스트 answer를 inf로 바꿔주고 해결
#정확성 테스트에서 한문제 틀리던 케이스는 마지막 if문에서 k를 k-1로 바꿈ㅁ

from collections import deque
def solution(stones, k):
    answer = float('inf')
    temp = deque()

    for i in range(len(stones)):
        new_stone = stones[i]
        while temp and temp[-1][1] <= new_stone:
            temp.pop()
            
        if temp and temp[0][0]+(k-1) < i:
            temp.popleft()
            
        temp.append([i,new_stone])
        
        if i >= k-1:
            answer = min(answer, temp[0][1])
            
    return answer