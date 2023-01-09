import collections
def solution(k, t):
    
    counter = collections.Counter(t)
    
    for i,(_,v) in enumerate(sorted(counter.items(), key=lambda x: x[1], reverse=True)):
        k -= v 
        if k <= 0:
            answer = i+1
            break
    return answer