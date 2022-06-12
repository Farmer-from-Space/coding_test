def solution(numbers):
    answer = 0

    split_nums = [i for i in numbers]
    # 숫자들의 모든 조합을 만들어서 하나씩 아래 num에 포문으로 넣어주면 될듯
    # 근데 조합을 못만들겠다


    # 에라토스테네스의 체 방식으로 소수를 구하는 법(이해못함)
    # https://blog.naver.com/nkj2001/222658000054

    prime_lists = [False, False] + [True] * (num - 1)

    primes = []

    for i in range(2, num + 1):
        if prime_lists[i]:
            for j in range(2*i, num+1, i):
                prime_lists[j] = False
    primes = [i for i in range(2, num+1) if prime_lists[i] == True]

    if num in primes:
        answer += 1

    return answer
# %%
