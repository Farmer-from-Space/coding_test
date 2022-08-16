#%%
n, m = map(int, input().split())

board = []
all = []
for _ in range(n):
    board.append(input())
for i in range(m-8+1):
    for j in range(n-8+1):
        wrong = 0
        for ii, h in enumerate(board[j:j+8]):
            
            for k in range(8):
                if ii%2 and k%2 :
                    if h[i:i+8][k]== 'W':
                        wrong += 1
                elif ii%2==0 and k%2==0:
                    if h[i:i+8][k]== 'W':
                        wrong += 1
                elif ii%2 and k%2==0 :
                    if h[i:i+8][k]== 'B':
                        wrong += 1
                elif ii%2==0 and k%2:
                    if h[i:i+8][k]== 'B':
                        wrong += 1


        all.append(min(wrong, 64-wrong))
            
        
print(min(all))    
        



# %%
0%2
# %%
