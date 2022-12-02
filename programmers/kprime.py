def solution(n, k):
    answer = 0
                
    # n을 k진수로 변환
    j = []         
    while n > 0 :
        j.insert(0, str(n % k))
        n //= k
    
    # 0사이에 끼어있는 숫자들을 리스트로 구하고
    num_list = [ int(i) for i in ''.join(j).split('0') if i != '']
    
    # 소수 구함
    target = max(num_list)
    prime = [0, 0] + [1] *target
    for i in range(2, int(target**.5)):
        for j in range(i*2, target, i):
            prime[j] = 0
    
    # 소수인지 판별
    for i in num_list:
        if prime[i]:
            answer += 1
    
    return answer


'''위에처럼 풀었다가 런타임 오류때문에 소수를 하나하나 판정하기로 함'''

def solution(n, k):
    answer = 0
                
    # n을 k진수로 변환
    j = []         
    while n > 0 :
        j.insert(0, str(n % k))
        n //= k
    
    # 0사이에 끼어있는 숫자들을 리스트로 구하고
    num_list = [ int(i) for i in ''.join(j).split('0') if i != '' and i != '1']
    
    for i in num_list:
        temp = 0
        for j in range(2, int(i**.5)+1):
            if not i%j:
                temp += 1
        if temp == 0:
            answer += 1
    
    
    return answer