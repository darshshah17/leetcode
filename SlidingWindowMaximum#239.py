import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maxHeap of size k? keep track of indices with hashmap

        # but how do we remove the val at nums[l] and add the new
        # nums[r] each iteration without knowing where it would fall
        # in the maxHeap (would depend on its val compared to others)

        # needed hint for this part:
        # we don't care if any other value in our maxHeap is out of
        # bounds of the current window except the max one. When the
        # max one is out of bounds, keep popping the max value until
        # max is no longer out of bounds
        l = 0
        r = k - 1
        res = []

        # heapify is minHeap by default, just make vals - for maxHeap
        heap = [(-nums[i], i) for i in range(l, r+1)]
        heapq.heapify(heap)

        while r < len(nums):
            while heap and (heap[0][1] < l or heap[0][1] > r):
                heapq.heappop(heap)
            res.append(-heap[0][0])

            l += 1
            r += 1

            if r >= len(nums):
                break
            heapq.heappush(heap, (-nums[r], r))


        return res