#%%
import sys
input = sys.stdin.readline


a, b = map(int, input().split())
a_list = set(map(int, input().split()))
b_list = list(map(int, input().split()))
count = a+b
    
for j in b_list:
    if j in a_list:
        count -= 2
print(count)
# %%
a, b = map(int, input().split())
a_list = set(map(int, input().split()))
b_list = set(map(int, input().split()))
    
print(len(a_list-b_list)+len(b_list-a_list))
# %%
# 리얼 집합적 풀이... 그림 그려보고 나서 이해했음
# print(2*len(set(a+b)) - (len(a)+len(b)))