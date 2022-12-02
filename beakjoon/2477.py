#%%
k =  int(input())
l = []
order =[4,2,3,1,4,2,3,1,4,2]
max_w, max_h =0, 0
w1, w2 = 0, 0
for i in range(6):
    side, lenth =  map(int, input().split())
    
    if side ==1 or side ==2:
        max_w =  max(max_w, lenth)
    else:
        max_h =  max(max_h, lenth)

    if i == 0:
        now = order.index(side)
    else:
        if order[now+i] != side and w1 ==0 :
            w1 = lenth
            w2 = l[-1][1]

    l.append([side,lenth])
    
if w1 == 0:
    w1 = l[0][1]
    w2 = l[-1][1]

print(k*(max_w*max_h-w1*w2))


# %%
