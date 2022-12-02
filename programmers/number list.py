# %%
# def solution(phone_book):
    
#     for i in range(len(phone_book)):
#         for j in range(len(phone_book)):
#             if j != i:
#                 if phone_book[j].startswith(phone_book[i]):
#                     return False
                    
#     return True
# %%
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
# %%
def solution(phone_book):
    answer = True
    hash_map = {}
    
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number: # 본인이 아니면서 hash_map에 있으면
                answer = False
                
    return answer
#%%
