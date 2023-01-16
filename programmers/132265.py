# 이렇게 풀긴 했지만 deque는 불필요하고, defaultdict는 set으로 대체해도 될것같다.

from collections import deque, Counter, defaultdict
def solution(topping):
    answer = 0
    
    l,r = deque(), deque(topping)
    ldict,rdict = defaultdict(int), Counter(r)
    
    for i in range(1, len(topping)):
        
        toss = r.popleft()
        rdict[toss] -= 1
        if rdict[toss] == 0:
            rdict.pop(toss)
            
        ldict[toss] += 1
        l.append(toss)
        
        if len(ldict) == len(rdict):           
            answer += 1
        
    return answer