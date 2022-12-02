class Solution:
    def isPalindrome(self, s) :
        s = [ i.lower() for i in s if i.isalnum()]
        sr = list(reversed(s))
        
        if s != sr:
            return False
        else:
            return True
    
            
        