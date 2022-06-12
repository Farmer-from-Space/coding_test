#%%
def solution(answers):
    soopoja1 = [1,2,3,4,5]
    soopoja2 = [2,1,2,3,2,4,2,5]
    soopoja3 = [3,3,1,1,2,2,4,4,5,5]

    while len(soopoja1) < len(answers):
        soopoja1 += soopoja1    
    while len(soopoja2) < len(answers):
        soopoja2 += soopoja2    
    while len(soopoja3) < len(answers):
        soopoja3 += soopoja3    


    count_num = [0,0,0]
    answer = []
    for i in range(len(answers)):
        if answers[i] == soopoja1[i]:
            count_num[0] += 1
        if answers[i] == soopoja2[i]:
            count_num[1] += 1
        if answers[i] == soopoja3[i]:
            count_num[2] += 1
  
    for i in range(len(count_num)):
        if max(count_num) == count_num[i]:
            answer.append(i+1)
    return answer

solution([1,3,2,4,2])
# %%
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []

#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1

#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)

#     return result
# %%
