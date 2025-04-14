from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        mostFreqChar = 0
        longestSubString = 0

        charFreq = defaultdict(int)

        while r < len(s):
            charFreq[s[r]] += 1

            # ------------------------------------------------------------
            # Option 1:
            # technically still O(1) bc len(charFreq) is capped at 26.
            # mostFreqChar = max(charFreq.values())

            # Option 2:
            # tricky to come up with but this method actually works bc you don't
            # need to decrement mostFreqChar whenever your left pointer moves up
            # because if the mostFreqChar var is ever less than what it used to be,
            # that subarray can never be your answer (aka the longest subarray)
            
            # math: (r - l + 1) - mostFreqChar > k, since we want to maximize
            # r - l + 1 but we want to minimize k, then we want to maximize 
            # mostFreqChar as well.
            mostFreqChar = max(mostFreqChar, charFreq[s[r]])

            # ------------------------------------------------------------

            while (r - l + 1) - mostFreqChar > k:
                charFreq[s[l]] -= 1
                l += 1

            longestSubString = max(longestSubString, r - l + 1)

            r += 1


        return longestSubString