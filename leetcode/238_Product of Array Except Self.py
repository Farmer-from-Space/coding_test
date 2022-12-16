class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
# 시간초과
#        def multiply(arr):
#            return eval('*'.join([str(n) for n in arr]))
#        ans = []
#        for i in range(len(nums)):
#            arr = nums[:i] + nums[i+1:]
#            ans.append(multiply(arr))
#        return ans
        p = 1
        out = []
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]
        
        p = 1
        for i in reversed(range(len(nums))):
            out[i] *= p
            p *= nums[i]
           
        return out