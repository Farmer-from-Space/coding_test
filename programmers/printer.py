# 80분 ㅜㅜㅜ
'''
처음에 for문으로 풀려다가 너무 오래걸리고 심지어 틀림.
- 막히거나 헤멘 부분 
1. 출력할 문서가 제일 뒤로가면 for문을 다시돌려야 되는점
2. for문이라 그때그때 remove or pop을 못해줘서 생기는 문제들 등

그냥 while문으로 바꾸고 5~10분만에 품.
시간을 체크하니까 조급해져서 못풀고 오히려 더 오래걸림.

'''
# %%
def solution(priorities, location):
    answer = 0
    while location > -1:
        if priorities[0] == max(priorities):
            answer += 1
            priorities.remove(priorities[0])
            location -= 1
        else:
            priorities.append(priorities[0])
            priorities.remove(priorities[0])
            
            if location == 0:
                location += len(priorities)-1
            else:
                location -= 1
            
    return answer
#%%
solution([1, 1, 9, 1, 1, 1], 0)
# %%






# def solution(priorities, location):
#     answer = 0
#     over = 0
#     while location > -1:
#         for i in range(len(priorities)):
#             if priorities[i] < max(priorities):
#                 priorities.append(priorities[i])
#                 over += 1
#                 if location == 0:
#                     location += len(priorities)
#             else:
#                 answer += 1
#                 priorities[i] = 0
#                 over += 1
#                 if location == 0:
#                     location -= 1  
#                     break
#             location -= 1  
#         priorities = priorities[over-1:]  
#     return answer
