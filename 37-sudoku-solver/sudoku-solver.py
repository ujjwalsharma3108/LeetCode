class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Existing numbers ko sets mein store karo
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    dig = board[i][j]

                    rows[i].add(dig)
                    cols[j].add(dig)
                    boxes[(i // 3) * 3 + (j // 3)].add(dig)

        def reoccurTask(board, i, j):

            if i == len(board):
                return True

            if j == 9:
                return reoccurTask(board, i + 1, 0)

            if board[i][j] != ".":
                return reoccurTask(board, i, j + 1)

            box = (i // 3) * 3 + (j // 3)

            for dig in range(1, 10):

                dig = str(dig)

                if isSafe(i, j, dig):

                    board[i][j] = dig

                    rows[i].add(dig)
                    cols[j].add(dig)
                    boxes[box].add(dig)

                    if reoccurTask(board, i, j + 1):
                        return True

                    # BACKTRACK
                    board[i][j] = "."

                    rows[i].remove(dig)
                    cols[j].remove(dig)
                    boxes[box].remove(dig)

            return False

        def isSafe(i, j, dig):

            box = (i // 3) * 3 + (j // 3)

            if dig in rows[i]:
                return False

            if dig in cols[j]:
                return False

            if dig in boxes[box]:
                return False

            return True

        reoccurTask(board, 0, 0)