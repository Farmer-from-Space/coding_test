#%%
n = int(input())

# n보다 작은 숫자중 소수만 리스트에 담는다.
ys  = int(n**0.5)+1
yslist = set(range(2, ys))

for i in range(2, ys):
    yslist -= set(range(i*2, ys, i))
yslist = list(yslist)

# 리스트의 작은수부터 n에 나눠보고 약수인 경우 출력
j = 0
while j != len(yslist) and n != 1:

    if n%yslist[j] == 0:
        print(yslist[j])
        n = n//yslist[j]
    else:
        j += 1
    if n in yslist:
        break
if n != 1:
    print(n)
# %%
n = int(input())
i = 2
r = int(n ** 0.5)

while i <= r:
    while not n % i:
        print(i)
        n //= i
    i += 1
if n > 1:
    print(n)

# %%
