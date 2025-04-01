class Solution:
    def findMin(self, nums: List[int]) -> int:
        # result will be arr[j] where j is the # of times rotated
        # do normal bin. search, except we're looking for the rotations
        # we'll know its the rotated val, bc the val before and after 
        # will both be greater
        # to account for the last val, we can do %

        # My soln (works, but cleaner soln at the bottom)
        l = 0
        r = len(nums)-1

        if len(nums) == 1:
            return nums[0]

        while l <= r:
            m = (l + r) // 2

            # min value (found the result)
            if nums[m - 1] > nums[m] and nums[(m + 1) % len(nums)] > nums[m]:
                return nums[m]
            # max value (result is the next value) 
            elif nums[m - 1] < nums[m] and nums[(m + 1) % len(nums)] < nums[m]:
                return nums[(m + 1) % len(nums)]
            # in a sequential block (e.g 2,3,4 - at 3)
            else:
                if nums[0] > nums[m]:
                    r = m - 1
                else:
                    l = m + 1


        # Not my soln but cleaner (also works)
        # l = 0
        # r = len(nums) - 1

        # if len(nums) == 1:
        #     return nums[0]

        # while l <= r:
        #     m = (l + r) // 2

        #     if nums[m-1] > nums[m] and nums[(m+1) % len(nums)] > nums[m]:
        #         return nums[m]
        #     elif nums[m] < nums[r]:
        #         r = m - 1
        #     else:
        #         l = m + 1