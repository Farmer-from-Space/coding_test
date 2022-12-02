#%%
import sys
input =  sys.stdin.readline

while True :
    n = int(input())
    if n == 0:
        break
    sosu =  set(range(n+1, n*2+1))
    sosu -= {1}
    bounds =  int((n*2)**0.5) +1

    for i in range(2, bounds):
        sosu -= set(range(i*2, n*2+1, i))
    print(len(sosu))
# %%

# 처음 리스트에서 2를 제외한 짝수는 다 빼버리고
# 홀수만 탐색해서 소수 판별을 하니까 속도가 훨씬 빨라짐

import sys
input =  sys.stdin.readline

while True :
    n = int(input())
    if n == 0:
        break
    sosu =  set([i for i in range(n+1, n*2+1) if i%2 or i ==2])
    
    bounds =  int((n*2)**0.5) +1

    for i in range(3, bounds, 2):
        sosu -= set(range(i*2, n*2+1, i))
    print(len(sosu))
# %%
# 퍼온코드 

# n의 최대제한인 123456 *2 까지의 소수를 구함
t = 246912

# 0,1은 0으로 채우고 나머지는 전부 1로 채운 리스트를 만들어서
# 소수가 아닌숫자만 0으로 바꿔줄 예정
x = [0, 0]+[1]*(t-1)

# 제거할 i배수의 i 범위
for i in range(int(t**.5) + 1):

# 예를들어 i가 3이면 3의 배수는 t의 1/3
# 해당개수만큼 i씩 건너뛰면서 0으로 바꿔준다
# 3은 지우면 안되기 때문에 *2부터 시작하고, [0]을 -1개 해준다.
    if x[i]: 
        x[2*i::i] = [0]*(t//i - 1) 

# 0이 입력되면 종료되는 while문
# 1,0으로 이루어진 리스트라 n ~ 2n의 범위의 합을 구하면 답이 나온다.
while True:
    n = int(input())

    if n == 0: 
        break

    print(sum(x[n + 1 : 2 * n + 1]))


# %%
