#157

a =  list(map(int, input().split()))
a = a[:-1]
b=[]
for i in a:
    if i%5==0:
        b.append(i)

print(f"Multiples of 5 : {len(b)}")
print(f"sum : {sum(b)}")
print(f"avg : {sum(b)/len(b):.1f}")