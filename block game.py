# https://programmers.co.kr/learn/courses/30/lessons/42894
#%%
def solution(board):
    answer = 0
    
    # 맨 위의 블럭부터 탐색하도록 순서 지정
    sum_board = sum(board,[])
    num_order = []
    for i in sum_board:
        if i != 0 and i not in num_order:
            num_order.append(i)
    
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

solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]])
# %%
