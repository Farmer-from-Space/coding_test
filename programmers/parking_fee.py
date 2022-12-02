def solution(fees, records):
    from math import ceil
    from collections import defaultdict
    
    base_time = fees[0]
    base_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    car_in = defaultdict(int) 
    car_out = defaultdict(int) 
    answer = []
    
    for i in records:
        i = list(map(str, i.split()))
        if i[2] == 'IN':
            car_in[i[1]] = int(i[0][:2])*60 + int(i[0][3:])
            
        else:
            car_out[i[1]] += (int(i[0][:2])*60 + int(i[0][3:])) - car_in[i[1]]
            car_in.pop(i[1])
    if car_in:
        for c_num, t in car_in.items():
            car_out[c_num] += (23*60 + 59) - t
            
    
    
    for k, v in sorted(car_out.items(), key= lambda x: x[0]):
        if v <= base_time:
            answer.append(base_fee)
        else:
            v -= base_time
            v = ceil(v/unit_time)
            answer.append(base_fee + (v*unit_fee))
            
            
    return answer