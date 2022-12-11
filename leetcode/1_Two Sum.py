class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            j = target-nums[i]
            if j in nums and nums.index(j) != i:
                j = nums.index(j)
                return [i, j]
