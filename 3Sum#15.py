class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Good soln - O(n^2) - doesnt pass all test cases for some reason
        # numIndex = {}
        # res = []
        # resSet = set()

        # for i, num in enumerate(nums):
        #     numIndex[num] = i
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         target = -1 * (nums[i] + nums[j])

        #         if target in numIndex and numIndex[target] != i and numIndex[target] != j:
        #             triplet = [nums[i], nums[j], target]
        #             triplet.sort()
        #             if tuple(triplet) not in resSet:
        #                 res.append(triplet)
        #                 resSet.add(tuple(triplet))

        # return res


        # Different Soln but passes all cases for some reason - O(n^2)
        nums = sorted(nums)
        res = []
        resSet = set()

        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            target = -1 * num

            while l < r:
                if nums[l] + nums[r] == target:
                    triplet = [nums[l], nums[r], num]
                    triplet.sort()

                    if tuple(triplet) not in resSet:
                        resSet.add(tuple(triplet))
                        res.append(triplet)

                    l += 1
                    r -= 1

                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1

        return res

        #Note for the second soln:
        #to optimize further, we can avoid the use of sorting the triplet and the extra memory of the resSet
        # - since the array is sorted, we can have a clause at the start of the for loop that says if i > 0 and nums[i] == nums[i-1], continue
        # - similarly, once a triplet matches, do res append the triplet, l += 1, and then if nums[l] == nums[l-1] and l < r, then l += 1
        # This automatically avoids all duplicates so we dont need to check for them anymore