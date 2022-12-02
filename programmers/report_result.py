# 좀 깔끔하지 못하게 푼거같아서 불만..

def solution(id_list, report, k):
    from collections import defaultdict
    
    answer = [0] * len(id_list)
    bad_users = defaultdict(list)
    for i in report:
        report_user, bad_user = i.split()
        if report_user not in bad_users[bad_user]:
            bad_users[bad_user].append(report_user)
        
    for b,r in bad_users.items():
        if len(r) >= k:
            for i in r:
                answer[id_list.index(i)] += 1
    
    
    return answer