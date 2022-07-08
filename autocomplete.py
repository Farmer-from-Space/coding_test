# 2:20
#%%

def solution(words):
    answer = 0    
    for i in range(len(words)):

        _words = words.copy()
        now = _words.pop(i)
        
        for j in range(len(now)):
            temp = 0
            for k in range(len(_words)):
                # 입력하는 문자가 다른 문자보다 짧을때.
                if len(_words[k]) >= len(now):
                    if _words[k][j] == now[j]:
                        temp += 1
                    elif j!= 0  and _words[k][j] != now[j] and _words[k][j-1] == now[j-1]:
                        temp += 1
                        
                # 입력하는 문자가 다른 문자보다 길어서, 인덱싱 지정이 넘칠때.
                elif len(_words[k]) > j:
                    
                    if _words[k][j] == now[j]:
                        temp += 1
                    elif j!= 0  and _words[k][j] != now[j] and _words[k][j-1] == now[j-1]:
                        temp += 1
                
                elif len(_words[k]) == j:
                    
                    if j!= 0 and _words[k][j-1] == now[j-1]:
                        temp += 1                   
                                            
            if temp > 0 :
                answer += 1
                            
    return answer

#%%

solution(["go","gone","guild"])
# %%
aa = ["go","gone","guild"]

bb = aa.copy()
aa.pop(0)

print(aa)
print(bb)
# %%
