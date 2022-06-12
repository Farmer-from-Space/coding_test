#%%
def solution(brown, yellow):
    temp=[]
    temp2=[]
    answer = []
    total = brown + yellow
    for i in range(3, total):
        if total % i == 0:
           temp.append(i)
    temp.sort(reverse=True)
    for i in temp:
        if total/i in temp:
            temp2.append(i)
    if len(temp2) == 1:
            answer.append(temp2[0])
            answer.append(temp2[0])
    elif len(temp2) > 2:
           answer.append(temp2[int(len(temp2)/2)-1])
           answer.append(temp2[int(len(temp2)/2)])
    else:
        answer = temp2
    return answer

solution(22, 8)
# %%
