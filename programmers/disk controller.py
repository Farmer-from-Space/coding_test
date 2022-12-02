# 18:04~
# 하루종일 품
# %%
import heapq
def solution(jobs):
    re_jobs=[]
    # input을 요청시간 순으로 정렬
    heapq.heapify(jobs)

    # spend_time = 첫번째 순번 요청부터 종료 소요시간
    spend_time=[jobs[0][1]]
    
    # now = 종료된 현재시간
    now = sum(heapq.heappop(jobs))

    # 작업시간 순으로 탐색하기 위해 작업시간을 앞으로 reverse
    for i in jobs:
        i.reverse()
        re_jobs.append(i)
    
    # 요청이 현재시간 이전에 들어온 작업들(possible) 
     
    while re_jobs:
        possible = []
        impossible = []
        for _ in range(len(re_jobs)):
            
            if re_jobs[0][1] <= now:
                possible.append(re_jobs.pop(0))
            else:
                impossible.append(re_jobs.pop(0))

    # 만약 while문을 계속 돈다면, 현재시간 이후에 요청되는 작업만 남음
    # 남은 해당작업도 possible에 넣어줘야 함
        if len(possible) == 0:
            possible = impossible
            impossible = []
            
    # possible중 가장 소요시간이 적은 작업을 다음 작업으로 지정
        heapq.heapify(possible)
        next = heapq.heappop(possible)

    # 현재시간보다 이후에 시작되는 작업은 그 작업의 (요청시간+작업시간=현재시간)
        if now < next[1]:
            now = sum(next)
    # 나머지 일반적으로 현재시간 이전에 요청이 들어온 작업들은 (현재시간 + 작업시간 = 현재시간)
        else:
            now = now + next[0]

    # 현재시간 - 요청시간 = 총 소요시간
        spend_time.append(now - next[1])

    # 남은것들은 다시 원래 리스트로 들어가서 while문을 돈다.
        re_jobs = re_jobs + possible + impossible
    
    # 총 소요시간들의 평균(소수점 버림)
    answer = sum(spend_time)//len(spend_time)
    return answer
# %%
solution([[0, 3], [1, 9], [2, 6]])

#%%

import heapq
def solution(jobs):
    re_jobs=[]
    heapq.heapify(jobs)

    spend_time=[jobs[0][1]]
    now = sum(heapq.heappop(jobs))

    for i in jobs:
        i.reverse()
        re_jobs.append(i)
     
    while re_jobs:
        possible = []
        impossible = []
        for _ in range(len(re_jobs)):
            
            if re_jobs[0][1] <= now:
                possible.append(re_jobs.pop(0))
            else:
                impossible.append(re_jobs.pop(0))

        if len(possible) == 0:
            possible = impossible
            impossible = []
            
        heapq.heapify(possible)
        next = heapq.heappop(possible)

        if now < next[1]:
            now = sum(next)
        else:
            now = now + next[0]

        spend_time.append(now - next[1])

        re_jobs = re_jobs + possible + impossible
    
    answer = sum(spend_time)//len(spend_time)
    return answer

#%%
# 퍼온코드 예술임..

import heapq
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))