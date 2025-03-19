from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res = []

        # numToOcc = tuple(Counter(nums).items())

        # numToOcc = sorted(numToOcc, key=lambda x: x[1], reverse=True)

        # for i in range(k):
        #     res.append(numToOcc[i][0])

        # return res
        
        # Optimal Soln:
        # O(n) time and O(n) space where n = len(nums)
        res = []
        c = Counter(nums)

        freqArr = [[] for i in range(len(nums) + 1)]

        for num, occ in c.items():
            freqArr[occ].append(num)

        for i in range(len(freqArr) - 1, -1, -1):
            for num in freqArr[i]:
                res.append(num)
                k -= 1

                if k == 0:
                    return res