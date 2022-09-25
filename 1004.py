n = int(input())
x1,y1,x2,y2 =  map(int, input().split())

for _ in range(n):
    ans = 0
    t =  int(input())
    for _ in range(t):
        cx, cy, r = map(int, input().split())
        dist1 = ((x1-cx)**2+(y1-cy)**2)**.5
        dist2 = ((x2-cx)**2+(y2-cy)**2)**.5

        if dist1 < r and dist2 < r:
            pass
        elif dist1 < r or dist2 < r:
            ans += 1

    print(ans)    