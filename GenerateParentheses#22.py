class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = ""

        def backtrack(opened, closed):
            # since strs are immutable
            # another soln would be to pass curr as a parameter into backtrack
            nonlocal curr

            if opened == n and closed == n:
                # appending curr and not curr.copy() bc .copy() is needed when
                # the data type is mutable like lists (strings are not)
                res.append(curr)
                return 

            # Add an opening:
            if opened < n:
                curr += "("
                backtrack(opened + 1, closed)
                curr = curr[:-1]

            # Add a closing:
            if closed < opened:
                curr += ")"
                backtrack(opened, closed + 1)
                curr = curr[:-1]


        backtrack(0, 0)
        return res
