def solution(storey):
    answer = 0
    storey = list(map(int, str(storey)))
    storey.reverse()
    upper = 0
    
    for i in range(len(storey)):
        now = storey[i]
        now += upper
        
        if now > 5 or (now >= 5 and i < len(storey)-1 and storey[i+1] >= 5):
            answer += 10-now
            upper = 1
        else: 
            answer += now
            upper = 0
            
    answer += upper
    
    return answer