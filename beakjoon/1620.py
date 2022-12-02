#%%
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic1={}
dic2={}

for i in range(1, n+1):
    name = input().strip()
    dic1[i] = name
    dic2[name] = i
for i in range(m):
    name = input().strip()
    if name.isdigit():
        print(dic1[int(name)])
    else:
        print(dic2[name])

# %%
# 풀고나서 다른코드 보다보니까 DIC을 두개 쓸 필요는 없잖아?
# 하지만 신기하게도 메모리와 시간 둘다 좀더 높아짐.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic={}

for i in range(1, n+1):
    name = input().strip()
    dic[str(i)] = name
    dic[name] = i
for i in range(m):
    print(dic[input().strip()])