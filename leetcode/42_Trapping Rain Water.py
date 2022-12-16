class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = height[0]
        right_max = height[-1]
        left_now, right_now = 0, len(height)-1
        vol = 0
        
        while left_now < right_now:
            while left_max <= right_max:
                left_now += 1
                if left_max >= height[left_now]:
                    vol += left_max - height[left_now]
                else:
                    left_max = height[left_now]
                if left_now >= right_now:
                    break

            while left_max > right_max:
                right_now -= 1 
                if right_max >= height[right_now]:
                    vol += right_max - height[right_now]
                else:
                    right_max = height[right_now]
                

        return vol

'''class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = height[0]
        right_max = height[-1]
        left_now, right_now = 0, len(height)-1
        vol = 0
        
        while left_now < right_now:
            
            left_max = max(left_max, height[left_now])
            right_max = max(right_max, height[right_now])

            if left_max <= right_max:
                vol += left_max - height[left_now]
                left_now += 1
            else:
                vol += right_max - height[right_now]
                right_now -= 1

        return vol'''