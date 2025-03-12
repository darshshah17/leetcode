class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #brute force:
        # res = []

        # for i, s in enumerate(strs):
        #     if s == 0:
        #         continue

        #     curr = [s]
        #     charOcc1 = {}
        #     for char in s:
        #         if char in charOcc1:
        #             charOcc1[char] += 1
        #         else:
        #             charOcc1[char] = 1
            
        #     for j in range(i+1, len(strs)):
        #         charOcc2 = {}
        #         s2 = strs[j]

        #         if s2 == 0:
        #             continue

        #         for char in s2:
        #             if char in charOcc2:
        #                 charOcc2[char] += 1
        #             else:
        #                 charOcc2[char] = 1

        #         if charOcc1 == charOcc2:
        #             curr.append(s2)
        #             strs[j] = 0
            
        #     res.append(curr)

        # return res


        #optimal soln:
        res = []
        occToWord = defaultdict(list)
        for s in strs:
            letterOccurence = [0] * 26

            for letter in s:
                letterOccurence[ord(letter) - ord("a")] += 1

            occToWord[tuple(letterOccurence)].append(s)

        
        for key in occToWord:
            res.append(occToWord[key])

        return res