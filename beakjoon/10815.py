#%%
n = int(input())
ns = sorted(list(map(int, input().split())))
m = int(input())
ms = list(map(int, input().split()))

for i in range(len(ms)):
    start,end= 0, n-1
    while start <= end:
        mid = (end+start) //2
        if ms[i] == ns[mid]:
            ms[i] = 1
            break
        elif ms[i] < ns[mid]:
            end = mid-1
        elif ms[i] > ns[mid]:
            start = mid+1
    if start > end:
        ms[i] = 0
    
print(*ms)
# %%
'''
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
'''
# 아래는 참고해볼 코드
"""
for i in range(len(card_comp)):
    if card_comp[i] in card_owned:
        print('1' + " ")
    else:
        print('0' + " ")
맨처음에는 in연산자로 하려했으나 천만개라는 숫자의 반복으로 시간초과 발생 해쉬 기법으로 시간복잡도가 낮은 
딕셔너리 자료형을 사용하여 반복을 줄이려고 생각"""


# from sys import stdin, stdout
# input = stdin.readline
# print = stdout.write


# N = int(input())
# card_owned = {}

# lst = input().split()
# for i in range(N):
#     card_owned[int(lst[i]) + 10000000] = '1'

# M = int(input())
# card_comp = input().split()
# for i in range(M): #비교값이 주어질때 원래 가지고 있는 카드 리스트를 일일이 순회할필요 없음
#     print(card_owned.get(int(card_comp[i]) + 10000000,'0') + " ")



#위 코드를 참고해서 읽기 편하게 고쳐봄
#%%

n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

sanggeun_cards = {}
for i in ns:
    sanggeun_cards[i+10000000] = 1
for j in ms:
    print(sanggeun_cards.get(j+10000000, 0), end =' ')


#%%