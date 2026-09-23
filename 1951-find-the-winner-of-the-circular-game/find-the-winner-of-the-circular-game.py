class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n + 1))

        def solve(present, remaining):
            if remaining == 1:
                return next(x for x in arr if x != -1)

            count = 0

            while count < k:
                if arr[present] != -1:
                    count += 1

                if count < k:
                    present = (present + 1) % n

            arr[present] = -1

            return solve((present + 1) % n, remaining - 1)

        return solve(0, n)
        

        