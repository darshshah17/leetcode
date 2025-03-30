class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find the row that the target should be in (up down):
        u = 0
        d = len(matrix) - 1

        while u <= d:
            mv = (u + d) // 2

            if matrix[mv][0] <= target and matrix[mv][-1] >= target:
                break
            elif matrix[mv][0] <= target:
                u = mv + 1
            else:
                d = mv - 1

        # Once the row is found, find the column like normal 1D binary search
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            mh = (l + r) // 2

            if matrix[mv][mh] > target:
                r = mh - 1
            elif matrix[mv][mh] < target:
                l = mh + 1
            else:
                return True
        
        return False

        # Overall time = log(m) + log(n) = log(m * n)
        