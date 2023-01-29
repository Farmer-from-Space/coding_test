# 2단계의 난이도가 갈수록 올라가는거 같다
def solution(maps):
    answer = []
    maps = [list(i) for i in maps]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for m in range(len(maps)):
        for i in range(len(maps[m])):
            if maps[m][i] != 'X':
                
                togo = []
                togo.append((m,i))
                answer.append(0)
                while togo:
                    y, x = togo.pop()
                    if maps[y][x] == 'X':
                        continue
                    answer[-1] += int(maps[y][x])
                    maps[y][x] = 'X'
                    for i in range(4):
                        ny , nx = y+dy[i], x+dx[i]
                        if (0 <= nx < len(maps[0]) and 0 <= ny <len(maps)) and maps[ny][nx] !='X' :
                            togo.append((ny,nx))
    if not answer:
        answer.append(-1)
        
    return sorted(answer)