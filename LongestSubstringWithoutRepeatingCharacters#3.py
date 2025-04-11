class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        r = 0
        res = 0
        currCount = 0

        while r < len(s):
            while r < len(s) and s[r] not in charSet:
                charSet.add(s[r])
                r += 1
                currCount += 1
                res = max(currCount, res)

            while l < r and r < len(s) and s[r] in charSet:
                charSet.remove(s[l])
                currCount -= 1
                l += 1

        return res


        