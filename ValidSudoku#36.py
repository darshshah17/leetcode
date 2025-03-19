from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #brute force (O(n^3))
        # nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        # # columns
        # colSet = set()
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] in nums and board[i][j] in colSet:
        #             return False
        #         else:
        #             colSet.add(board[i][j])

        #     colSet.clear()

        # # rows
        # rowSet = set()
        # for i in range(9):
        #     for j in range(9):
        #         if board[j][i] in nums and board[j][i] in rowSet:
        #             return False
        #         else:
        #             rowSet.add(board[j][i])

        #     rowSet.clear()

        # # 3x3
        # squareSet = set()
        # for i in range(0, 9, 3):
        #     for j in range(0, 9, 3):
        #         for k in range(3):
        #             for l in range(3):
        #                 if board[i + k][j + l] in nums and board[i + k][j + l] in squareSet:
        #                     return False
        #                 else:
        #                     squareSet.add(board[i + k][j + l])

        #         squareSet.clear()

        # return True

        # Better solution (first 2 parts are the same, 3x3 part is different)
        # O(n^2)
        nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        # columns
        colSet = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] in nums and board[i][j] in colSet:
                    return False
                else:
                    colSet.add(board[i][j])

            colSet.clear()

        # rows
        rowSet = set()
        for i in range(9):
            for j in range(9):
                if board[j][i] in nums and board[j][i] in rowSet:
                    return False
                else:
                    rowSet.add(board[j][i])

            rowSet.clear()

        # 3x3
        squareDict = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] in nums and board[i][j] in squareDict[(i // 3, j // 3)]:
                    return False
                else:
                    squareDict[(i // 3, j // 3)].add(board[i][j])
                

        return True