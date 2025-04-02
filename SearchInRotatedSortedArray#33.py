class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Got a hint on what to do after finding the rotation point
        # (doing bin. search on each of the sections)

        # might be easier doing part 1 in a separate function 

        # part 1: find the index of rotation (done myself)
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m-1] > nums[m] and nums[(m+1) % len(nums)] > nums[m]:
                break
            elif nums[m-1] < nums[m] and nums[(m+1) % len(nums)] < nums[m]:
                m = (m+1) % len(nums)
                break
            else:
                if nums[m] > nums[0]:
                    l = m + 1
                else:
                    r = m - 1
        
        # part 2: do bin. search on each of the parts 
        # (before and after rotation point) - got hint on this

        l = 0
        r = m - 1

        while l <= r:
            m2 = (l + r) // 2

            if nums[m2] == target:
                return m2
            elif nums[m2] > target:
                r = m2 - 1
            else:
                l = m2 + 1

        l = m
        r = len(nums) - 1

        while l <= r:
            m2 = (l + r) // 2

            if nums[m2] == target:
                return m2
            elif nums[m2] > target:
                r = m2 - 1
            else:
                l = m2 + 1

        return -1

        