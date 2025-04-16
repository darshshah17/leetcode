from collections import defaultdict, Counter

class Solution:
    def charReqMet(self, sDict, tDict):
        for char in tDict:
            if sDict[char] < tDict[char]:
                return False

        return True


    def minWindow(self, s: str, t: str) -> str:
        # Logic:
        # start from beginning, then increment r until a valid substring is found.
        # Then, increment l until its no longer valid, then continue this until r 
        # crosses the end. Each time a valid substring is found, compare it to our
        # existing shortest one.

        # Runs in O(n) because the function above (charReqMet) iterates tDict which is capped at 26.
        # We could've used an array of length 26 to prove this and show it clearly.

        # note: the reason we're using r - l and s[l:r] instead of l + 1 is because
        # the way the first inner while loop works is by the time you hit your desired 
        # answer (the first substring when charReqMet is True, it'll be evaluating  
        # sDict[s[r]] from the previous run since r has incremented one more time   
        # since then). Therefore, when we go to the 2nd inner loop, r will be 1 past
        # our desired result, so s[l:r] works.
        # I kinda stumbled onto that part accidentally.

        l = r = 0

        sDict = defaultdict(int)
        tDict = Counter(t)
        res = ""

        while r < len(s):
            while r < len(s) and not self.charReqMet(sDict, tDict):
                sDict[s[r]] += 1
                r += 1
            
            while l <= r and self.charReqMet(sDict, tDict):
                if len(res) == 0 or len(res) > r - l:
                    res = s[l:r]
                
                sDict[s[l]] -= 1
                l += 1

        return res