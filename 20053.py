#%%
import sys, io
file = open('input.txt', 'w')
data = '''3
5
20 28 22 25 21
5
30 21 17 25 29
5
20 10 35 30 7
'''

file.write(data)
file.close()
input_file = open('input.txt', 'r')
sys.stdin = io.StringIO(input_file.read())
#%%
import sys
input =  sys.stdin.readline

T = int(input())
for _ in range(T):
        N = int(input())
        digits = list(map(int, input().split()))
        print(min(digits), max(digits))
# %%
