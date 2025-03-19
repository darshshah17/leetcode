class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Brute force (not even sure if its O(n)) - doesnt pass all cases
        # n = set(nums)
        # longest = 0

        # for num in n:
        #     i = 0
        #     while num + i in n:
        #         i += 1

        #     longest = max(longest, i)

        # return longest

        # Optimal soln 
        n = set(nums)
        longest = 0

        for num in n:
            if num - 1 not in n:
                i = 1
                while num + i in n:
                    i += 1

                longest = max(longest, i)

        return longest

        