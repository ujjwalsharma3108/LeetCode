class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        # Find the minimum possible maximum difference.
        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        limit = left

        # Reduce every difference to at most limit.
        ans = sum(min(d, limit) ** 2 for d in diff)

        # Use the remaining operations on values equal to limit.
        remaining = k - sum(max(0, d - limit) for d in diff)

        ans -= remaining * (2 * limit - 1)

        return ans
