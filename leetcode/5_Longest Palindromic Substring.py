class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # 시간초과 코드
        # longest=''
        # for i in range(len(s)):
        #     for j in range(len(s), 0+i, -1):
        #         if s[i] == s[j-1]:
        #             temp = s[i:j]
                    
        #             if  temp == temp[::-1]:
        #                 longest= max(longest, temp)
        # return longest

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        if len(s) < 2  or s == s[::-1]:
            return s
        
        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        
        return result
    