#155

a =  input()
jungol = ['J', 'U', 'N', 'G', 'O', 'L']

for i in range(len(jungol)):

    if a == jungol[i]:
        print(i)
    elif a not in jungol:
        print('none')
        break