# 25분정도?걸림. 이런방식으로 풀면 너무 시간이 오래걸릴거 같은데 괜찮나?


#%%
n =  int(input())

maxfive = n//5

while (n-(maxfive*5))%3 != 0:
    maxfive -= 1
    if maxfive < 0:
        print(-1)
        break

if maxfive >= 0:
    print(maxfive + ((n-(maxfive*5))//3))
# %%
