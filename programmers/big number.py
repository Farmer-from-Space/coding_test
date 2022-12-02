#%%

def solution(number, k):
    selec= []
        
    for i in number:
        while selec and selec[-1] < i and k > 0 :
            selec.pop()
            k -= 1
            
        selec.append(i)
    
    if k != 0:
        selec = selec[:-k]

    answer = ''.join(selec)
   
    return answer

solution("1918888", 3)

# %%
