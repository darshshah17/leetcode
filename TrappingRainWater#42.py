class Solution:
    def trap(self, height: List[int]) -> int:
        #first pass: forward
        l = 0
        r = 1
        area = 0

        while r < len(height) and height[r] > height[l]:
            r += 1
            l += 1
        
        while r < len(height):
            currBlock = 0
            while r < len(height) and height[r] < height[l]:
                currBlock += height[r]
                r += 1
            
            if r < len(height):
                area += (min(height[r], height[l]) * (r-l-1) - currBlock)
            currBlock = 0
            l = r
            r += 1

        # 2nd pass: backward
        r = len(height)-1
        l = r - 1

        while l >= 0 and height[r] <= height[l]:
            r -= 1
            l -= 1
        
        while l >= 0:
            currBlock = 0
            while l >= 0 and height[l] <= height[r]:
                currBlock += height[l]
                l -= 1
            
            if l >= 0:
                area += (min(height[r], height[l]) * (r-l-1) - currBlock)
            currBlock = 0
            r = l
            l -= 1

        return area
        