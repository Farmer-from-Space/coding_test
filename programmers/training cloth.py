# 12:50
#체육복
#%%

def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    # student =  n - len(lost)
    # new_lost = []
    # for i in lost:
    #     if i in reserve:
    #         reserve.remove(i)
    #         student += 1
    #     else:
    #         new_lost.append(i)
    new_reserve = [ i for i in reserve if i not in lost]
    new_lost = [ i for i in lost if i not in reserve]

    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
            
        elif i+1 in new_lost:
            new_lost.remove(i+1)
            
    
    answer = n- len(new_lost)
    return answer

solution(5, [2, 4], [1, 3, 5])
# %%