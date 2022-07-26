#%%

def solution(clothes):
    answer = 1
    
    types = [y for x, y in clothes]
    counts = [types.count(t) for t in set(types)]
    for i in counts:
        answer *= i + 1
    
    return answer - 1

#%%

solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
# %%
