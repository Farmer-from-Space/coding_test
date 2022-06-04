successful = 0
for _ in range(5):
    score = list(map(int, input().split()))
    if sum(score)/len(score) >= 80:
        print('pass')
        successful +=1
    else:
        print('fail')
print(f'Successful : {successful}')
