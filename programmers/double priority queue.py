# 12:56~13:30(총34분)
# _heapify_max 기능을 사용하지 않고 풀어봐야 되겠다.
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
# 문제의도를 잘 반영한것처럼 보이는 코드 퍼옴.
# https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9D%B4%EC%A4%91%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%ED%81%90-%ED%9E%99
# 근데 remove를 사용 안하면 더 좋을거 같은디..
import heapq
def solution(operations):
    heap = []
    max_heap = []

    for o in operations:
        current = o.split()
        if current[0] == 'I':
            num =  int(current[1])
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (num*-1, num))
        else:
            if len(heap) == 0:
                pass
            elif current[1] == '1':
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)
            elif current[1] == '-1':
                min_value = heapq.heappop(heap)
                max_heap.remove((min_value*-1, min_value))
    if heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    else:
        return [0, 0]
# %%
