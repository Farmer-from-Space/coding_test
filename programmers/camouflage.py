#%%

def solution(clothes):
    answer = 1
    
    types = [y for x, y in clothes] # 의상의 타입들만 가져온다
    counts = [types.count(t) for t in set(types)] # 중복을 제거하고 타입별 몇개씩있는지 구하고, 곱해서 경우의 수를 구할예정
    for i in counts:
        answer *= i + 1 # 해당 타입의 의상을 아예 안입을 경우도 경우의 수에 추가해서 곱해준다
    
    return answer - 1 # 아무것도 안입은 경우의 수도 포함된 상태이므로 1을 빼준다

#%%

solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
# %%
