import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [ input() for _ in range(r)]

dx, dy = [1,-1,0,0], [0,0,1,-1]
need_visit =set()
def find(graph):
    answer = 0
    need_visit.add((0,0,graph[0][0]))
    while need_visit:
        x, y, visited = need_visit.pop()
        answer = max(answer, len(visited))
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if c > nx >= 0 and r > ny >= 0 and graph[ny][nx] not in visited:
                need_visit.add((nx,ny,visited+graph[ny][nx]))
    return answer

print(find(graph))
