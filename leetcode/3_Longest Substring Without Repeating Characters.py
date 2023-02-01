# 2중 for문으로도 풀리긴 한다
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            for j in range(i, len(s)+1):
                if len(s[i:j]) == len(set(list(s[i:j]))):
                    ans = max(ans, len(s[i:j]))
                else:
                    break
        return ans

# 해싱을 이용한 방법
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = collections.defaultdict(int)
        start = 0
        ans = 0
        for i,v in enumerate(s):
            if v in used and start <= used[v] :
                start = used[v] + 1
                used[v] = i
            else:
                ans =  max(ans, len(s[start:i+1]))
                used[v] = i