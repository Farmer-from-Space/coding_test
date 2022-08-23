#%%
def solution(n):
    jb = [4,1,2]
    num = []
    answer = ''
    while n != 0:
        num.append(n%3)
        if not n%3:
            n = (n//3)-1
        else:
            n = (n//3)

    for i in range(len(num)-1, -1, -1):
        answer += str(jb[num[i]])
    return answer

solution(10)
# %%