W, H, X, Y, P = map(int, input().split())
ans = 0
for _ in range(P):
    x1, y1 = map(int, input().split())
    dist1 = ((X-x1)**2+(Y+H/2-y1)**2)**.5
    dist2 = ((X+W-x1)**2+(Y+H/2-y1)**2)**.5

    if dist1 <= H/2 or dist2 <= H/2 or (X <= x1 <= X+W and Y <= y1 <= Y+H):
        ans += 1
print(ans)