class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            j = target-nums[i]
            if j in nums and nums.index(j) != i:
                j = nums.index(j)
                return [i, j]
