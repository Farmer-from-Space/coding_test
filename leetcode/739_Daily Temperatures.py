class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(t)
        for i, v in enumerate(t):

            while stack and t[stack[-1]] < v :
                last = stack.pop()
                ans[last] = (i - last)
            
            stack.append(i)

        
        return ans