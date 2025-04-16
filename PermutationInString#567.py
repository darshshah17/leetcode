from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # technically this still meets the requirement of O(1) 
        # space even though it doesnt seem that way bc each dict
        # is capped at length 26.
        
        l = 0
        r = len(s1)-1

        s1Dict = Counter(s1)
        s2Dict = Counter(s2[l:r+1])

        while r < len(s2):
            if s1Dict == s2Dict:
                return True

            s2Dict[s2[l]] -= 1
            if s2Dict[s2[l]] == 0:
                del s2Dict[s2[l]]

            l += 1
            r += 1

            if r >= len(s2):
                break

            s2Dict[s2[r]] += 1

        return False