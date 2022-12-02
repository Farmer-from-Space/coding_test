#%%
def solution(brown, yellow):
    temp=[]
    answer = []
    total = brown + yellow
    for i in range(3, total):
        if total % i == 0:
           temp.append(i)
    temp.sort(reverse=True)
    for i in temp:
        if total/i in temp and (total/i-2)*(i-2) == yellow :
            answer.append(i)
            answer.append(total//i)
            break
    return answer

solution(22, 8)
# %%
