# 4:43 ~ 5:35 총52분
# 첫코드는 20분정도 걸림
'''
count.append를 while문 안에 넣어주다보니 
마지막 카운트가 append되지 않고 종료되는걸 해결하는 방법이 틀려서 고치는데 오래걸림.
처음에 어디가 틀린줄 모르고 다른데서 헤멤
틀린 코드
if progresses[i] == progresses[-1]:
    answer.append(count)
'''
#%%

def solution(progresses, speeds):
    count =0
    answer = []
    for i in range(len(progresses)):
        while progresses[i] < 100:
            if count > 0:
                answer.append(count)
                count = 0
            for j in range(len(progresses)):
                progresses[j] += speeds[j]
        count += 1
        if i == len(progresses)-1:
            answer.append(count)

    return answer
#%%
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])
# %%