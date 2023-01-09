def recursion(s, l, r, i):
    if l >= r: return 1, i
    elif s[l] != s[r]: return 0, i
    else: 
        i +=1
        return recursion(s, l+1, r-1, i)

def isPalindrome(s):
    i = 1
    return recursion(s, 0, len(s)-1, i)

n = int(input())
for i in range(n):
    print(*isPalindrome(input()))
