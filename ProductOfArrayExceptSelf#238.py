class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force O(n^2):
        # res = []
        # for i in range(len(nums)):
        #     total = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
                
        #         total *= nums[j]

        #     res.append(total)

        # return res

        #Optimal soln O(n):
        res = [1] * len(nums)

        #1st pass:
        for i in range(1, len(nums)):
            res[i] *= (nums[i-1] * res[i-1])

        #2nd pass:
        for i in range(len(nums)-2, -1, -1):
            res[i] *= nums[i+1]
            nums[i] *= nums[i+1]

        return res