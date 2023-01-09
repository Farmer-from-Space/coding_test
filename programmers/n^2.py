# 첫번째 문제 설명 그대로의 풀이
def solution(n, left, right):
    dp = [[i for i in range(1, n+1)] for _ in range(n)]

    for i in range(n):
        dp[i][:i+1] = [i+1] * (i+1)

    dp = sum(dp, [])

    answer = dp[left: right+1]
    return dp

# 시간초과 나서 다시 푼 풀이
def solution(n, left, right):

    answer = []
    c = right - left
    
    left_d, left_rm = divmod(left, n)

    right_d, right_rm = divmod(right, n)
    
    left_d += 1
    right_d += 1
    
    while left_d < right_d+1:
        for i in range(1, n+1):
            if i < left_d:
                answer.append(left_d)
            else:
                answer.append(i)
        left_d += 1
    
    return answer[left_rm: left_rm+c+1]

# 남들 풀이..
def solution(n, left, right):
    answer = []

    for i in range(left, right+1):
        q, r = divmod(i, n)

        answer.append(max(q, r) + 1)

    return answer