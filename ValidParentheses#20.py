class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {"[": "]", "(": ")", "{": "}"}

        for c in s:
            if c in opening:
                stack.append(opening[c])
            else:
                if len(stack) == 0 or stack.pop() != c:
                    return False

        return len(stack) == 0