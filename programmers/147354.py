def solution(data, col, row_begin, row_end):
    answer = 0
    temp = []
    data.sort(key=lambda x: x[0], reverse=True)
    data.sort(key=lambda x: x[col-1])
    
    for i in range(row_begin-1, row_end):
        temp = 0
        for j in data[i]:
            temp += j%(i+1)
        answer ^= temp
    return answer