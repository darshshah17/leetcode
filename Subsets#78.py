class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []

    
        def backtrack(i):
            if i == len(nums):
                res.append(curr.copy())
                return

            # Don't add the curr val (nums[i])
            backtrack(i+1)

            # Add it
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()


        backtrack(0)
        return res


        