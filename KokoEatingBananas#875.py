class Solution:
    # version of isPossible I came up with (would also need to pass piles.copy() on line 31) that gives time limit exceeded. 
    
    # def isPossible(self, arr, rate, hours):
    #     for i in range(len(arr)):
    #         while arr[i] > 0:
    #             arr[i] -= rate
    #             hours -= 1

    #             if hours < 0:
    #                 return False
    #     return True
    
    def isPossible(self, arr, rate, hours):
        for i in range(len(arr)):
            if arr[i] % rate != 0:
                hours -= (arr[i] // rate + 1)
            else:
                hours -= arr[i] // rate

        return hours >= 0

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search with the value of k (min = 1, max = max(piles))
        lowest = 1
        highest = max(piles)
        res = 0

        while lowest <= highest:
            k = (lowest + highest) // 2

            if self.isPossible(piles, k, h):
                res = k
                highest = k - 1
            else:
                lowest = k + 1

        return res

        