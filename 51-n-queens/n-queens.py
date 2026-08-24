class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        ans = []

        def nQueens(row):

            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):

                if isSafe(row, col):

                    board[row][col] = "Q"

                    nQueens(row + 1)

                    board[row][col] = "."

        def isSafe(row, col):

            # column
            for r in range(row):
                if board[r][col] == "Q":
                    return False

            # upper-left diagonal
            r = row - 1
            c = col - 1

            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False

                r -= 1
                c -= 1

            # upper-right diagonal
            r = row - 1
            c = col + 1

            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False

                r -= 1
                c += 1

            return True

        nQueens(0)

        return ans
