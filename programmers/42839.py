from itertools import permutations
def solution(n):
    # 먼저 만들수 있는 숫자의 조합을 전부 구함.
    combi = set()
    for i in range(1, len(n)+1):
        for j in set(permutations(n, i)):
            combi.add(int("".join(j)))

    # 조합의 최대값까지 소수리스트를 구함.
    until = max(combi)
    prime = [0 , 0] + [1] * (until-1)
    
    for i in range(2, int(until**.5) +1):
        for j in range(i*2, until+1, i):
            prime[j] = 0
            
    # 조합에서 소수를 카운트
    ans = 0
    for i in combi:
        if prime[i] == 1:
            ans += 1
    return ans


''' 세트에서 세트를 제외해 한단계 줄인 방법'''

from itertools import permutations
def solution(n):
    # 먼저 만들수 있는 숫자의 조합을 전부 구함.
    combi = set()
    for i in range(1, len(n)+1):
        for j in set(permutations(n, i)):
            combi.add(int("".join(j)))

    # 조합의 최대값까지 소수가 아닌 수들을 찾아서 combi에서 빼줌.
    until = max(combi)
    combi -= set(range(0,2))
    for i in range(2, int(until**.5) +1):
        combi -= set(range(i*2, until+1, i))
    
    return len(combi)