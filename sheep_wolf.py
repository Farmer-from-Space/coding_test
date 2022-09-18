# 시간은 좀 걸렸지만 풀었다는 것에 의의..

def solution(info, edges):
    answer = 0
       
    can_visit = [i for i in edges if i[0] == 0 and info[i[1]] != 1]
    visiting = []
    if not can_visit:
        return 1
    while can_visit:
        
        visiting = can_visit.pop()
        wolf, sheep = 0, 0
                
        for i in visiting:
            if info[i]:
                wolf += 1
            else:
                sheep += 1
            
        answer = max(answer, sheep)
        
        for i in edges:
            if i[0] in visiting and i[1] not in visiting:
                if (info[i[1]] and sheep - (wolf+1) > 0) or not info[i[1]]:
                    can_visit.append(visiting + [i[1]])
        
    return answer