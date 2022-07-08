def solution(prices):
    answer = []

    for i in range(len(prices)):
        if i < len(prices)-1:
            count = 0

            if min(prices[i:]) == prices[i]:
                count += (len(prices)-1) - i
            else:
                for j in range(len(prices)-(i+1)):
                    while count == 0 :
                        if prices[i] > prices[i+j+1]:
                            count += j + 1

            answer.append(count)
        else:
            answer.append(0)

    return answer