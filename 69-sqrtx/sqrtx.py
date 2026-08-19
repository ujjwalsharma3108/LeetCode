class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        def search(left, right):

            if left > right:
                return right

            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            if mid * mid < x:
                return search(mid + 1, right)

            return search(left, mid - 1)

        return search(1, x)