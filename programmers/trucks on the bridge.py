# 100분 ㅜㅜ
'''
시간을 카운트하는 방식에서 헤멤
temp_sec을 만들었다가 지웠다가..

'''

#%%

def solution(bridge_length, weight, truck_weights):

    sec = 1
    done = []
    ing = []
    len_truck_weights = len(truck_weights)
    
    while len(done) < len_truck_weights:

        if truck_weights:

            if sum(ing)+truck_weights[0] <= weight:
                ing.append(truck_weights.pop(0))
            else:
                ing.append(0)
        else:
            ing.append(0)

        if bridge_length == len(ing) :

            if ing[0] != 0:
                done.append(ing.pop(0))
            else:
                ing.remove(ing[0])

        sec += 1

    answer = sec

    return answer

#%%

solution(100, 100, [10,10,10,10,10,10,10,10,10,10])
# %%
