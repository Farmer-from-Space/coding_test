# https://programmers.co.kr/learn/courses/30/lessons/42894
# 맨 아래에 있는 블럭을 마지막에 탐색하도록 순서 지정(이 부분 착오로 65점 나왔었음)
# 아래 예시처럼 위,왼쪽부터 순서를 정하면 1번부터 하게 되는데 사실은 2번부터 제거해야함.
# 위에 뭐가 먼저 나오느냐 X 뭐가 더 밑에 있냐 O 로 순서를 정해야 함.
'''
예시
0 0 0 0
1 0 0 2
1 2 2 2
1 1 0 0
'''

#%%
def solution(board):
    answer = 0
    
    # 맨 아래에 있는 블럭을 마지막에 탐색하도록 순서 지정(이 부분 착오로 65점 나왔었음)
    sum_board = reversed(sum(board,[]))
    num_order = []
    for i in sum_board:
        if i != 0 and i not in num_order:
            num_order.append(i)
    num_order.reverse()

    for i in num_order:
        temp = []
        im_num = 0
        # 블럭위에 아무것도 없는지 확인
        for g in range(len(board[0])):
                check = 0
                for h in range(len(board)-1, -1, -1):
                    if board[h][g] == i :
                        check += 1
                    elif check == 1 and board[h][g] != 0:
                        im_num += 1
        
        
        # 블럭의 형태가 지울수 있는 모양인지 확인
        for j in board:
            temp.append(j.count(i))
        for k in range(len(temp)):
            if k != 0 and temp[k]!= 0 and temp[k-1] > temp[k]:
                im_num += 1
        
        # 위 아무것도 없고, 지울수 있는 모양이면 answer를 추가하고 해당블럭 0으로 삭제        
        if im_num == 0:
            for h in range(len(board)):
                for g in range(len(board[0])):
                    if board[h][g] == i:
                        board[h][g] = 0
            answer += 1
                   
    
    return answer

#%%

solution([[0, 0, 0, 0, 0], [1, 0, 0, 2, 0], [1, 2, 2, 2, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]])
# %%
