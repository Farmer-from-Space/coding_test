while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    
    if a < b and not b%a:
        print('factor')
    elif a > b and not a%b:
        print('multiple')
    else:
        print('neither')