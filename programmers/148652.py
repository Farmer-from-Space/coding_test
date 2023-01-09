def solution(n, l, r):
    def count_num(num):
        if num <= 5: return '11011'[:num].count('1')
    
        j = 1
        while 5 ** (1+j) < num:
            j += 1
        
        m = num // (5**j)
        rm = num % (5**j)
        
        answer = m * (4 ** j)
        
        if m >= 3:
            answer -= (4 ** j)
        if m == 2:
            return answer
        else:
            return answer + count_num(rm)
        
    return count_num(r) - count_num(l-1)
