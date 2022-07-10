# 12:56~13:30(총34분)
#%%
import heapq
def solution(operations):
    queue = []
    answer = []
    for i in range(len(operations)):
        if operations[i].startswith('I'):
            heapq.heappush(queue, int(operations[i][2:]))
        elif operations[i].startswith('D 1'):
            if queue:
                heapq._heapify_max(queue)
                heapq._heappop_max(queue)
        elif operations[i].startswith('D -1'):
            if queue:
                heapq.heapify(queue)
                heapq.heappop(queue)
        
    if queue:
        heapq._heapify_max(queue)
        answer.append(heapq._heappop_max(queue))
        heapq.heapify(queue)
        answer.append(heapq.heappop(queue))
    else:
        answer = [0,0]
    
    return answer


# %%
solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
# %%
