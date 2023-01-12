# 시간초과로 안풀리던 테스트케이스가 한문제 있었는데 visited_set을 추가해서 해결

from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    answer = [10000000,100000000]
    visited = [10000001] *(n+1)
    graph = defaultdict(list)    
    summits = set(summits)
    for de, ar, t in paths:
        graph[de].append((t,ar))
        graph[ar].append((t,de))


    for gate in gates:
        togo = []#최대intensity, 코스
        heapq.heappush(togo,(0, gate))
        visited_set = set()
        while togo:
            
            now = heapq.heappop(togo)
            if now[1] in visited_set:
                continue
            visited_set.add(now[1])    
            if now[1] in summits:
                if now[0] < answer[1] or (now[0] == answer[1] and now[1] < answer[0]):
                    answer = [now[1], visited[now[1]]]
                                       
            else:
                for path in graph[now[1]]:
                    if visited[path[1]] > max(path[0], now[0]) :
                        visited[path[1]] =  max(path[0], now[0])
                        heapq.heappush(togo, ((visited[path[1]],)+(path[1],)))
                                
                
    return answer



