class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #steps:
        #1) make a hash map (num --> index)
        #2) look through nums and find target - num in the hash map

        numIndex = {}

        for i, num in enumerate(nums):
            numIndex[num] = i

        for i,num in enumerate(nums):
            if target - num in numIndex and i != numIndex[target - num]:
                return [i, numIndex[target - num]]

            
        