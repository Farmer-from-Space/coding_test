    # 에라토스테네스의 체 방식으로 소수를 구하는 법(이해못함)
    # https://blog.naver.com/nkj2001/222658000054


#%%
def solution(numbers):
    answer = 0
    all_nums = []
    from itertools import permutations
    for i in range(len(numbers)):
        permute = list(permutations(numbers,i+1))
        for j in range(len(permute)):        
            all_nums.append(int("".join(permute[j])))
    
    all_nums = set(all_nums)
    

    for num in all_nums:
        if num != 0 and num != 1:
            prime_lists = [False, False] + [True] * (num - 1)

            primes = []

            for i in range(2, num + 1):
                if prime_lists[i]:
                    for j in range(2*i, num+1, i):
                        prime_lists[j] = False
            primes = [i for i in range(2, num+1) if prime_lists[i] == True]
            
            if i in primes:
                answer += 1

    return answer
# %%
# 석진님 코드
# from itertools import permutations

# def solution(numbers):
#     prime_set = set()
#     for i in range(len(numbers)):
#         numbers_permutation = permutations(list(numbers), i  + 1)
#         numbers_per_list = map(int, map("".join, numbers_permutation))
#         prime_set |= set(numbers_per_list)

#     prime_set -= set(range(0, 2))
#     lim = int(max(prime_set) ** 0.5) + 1
#     for i in range(2, lim):
#         prime_set -= set(range(i * 2, max(prime_set) + 1, i))
#     answer = len(prime_set)

#     return answer