#152

a =  list(map(int, input().split()))
odd = 0
even = 0
for i in range(len(a)):
    if (i+1) % 2 == 0:
        even += a[i]
    else:
        odd += a[i]
print(f"odd : {odd}")
print(f"even : {even}")