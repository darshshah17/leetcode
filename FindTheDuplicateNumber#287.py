class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # naive soln: hashmap
        # O(n) time + O(1) space soln (got hint, but very hard problem):
        # treat them as linked lists, where the value at an index
        # is the index you go to each time. Use a slow/fast ptr to find 
        # the "cycle", which is how you know what the duplicate is
        # because if the value is where you go, if you end up somewhere
        # twice (slow/fast) that means two vals in the arr are the same
        
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                break

        # once you find what the duplicate is, hold the val of
        # slow because due to some math proof, the distance between
        # (where the slow and fast ptr meet) and (the start of the 
        # cycle) is the same distance between (the start of the 
        # cycle) and (the start of the array (slow2)) 
        # because of this ^ we can just use two slow ptrs and see
        # where they meet, which will be the start of the cycle
        # aka the duplicate value
         
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow

