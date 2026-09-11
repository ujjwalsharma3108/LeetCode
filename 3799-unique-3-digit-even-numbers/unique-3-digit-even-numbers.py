class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        ans = 0

        for first in range(1, 10):       # 1st digit: 1-9
            if freq[first] == 0:
                continue

            freq[first] -= 1

            for second in range(10):     # 2nd digit: 0-9
                if freq[second] == 0:
                    continue

                freq[second] -= 1

                for last in range(0, 10, 2):  # Last digit: even
                    if freq[last] > 0:
                        ans += 1

                freq[second] += 1

            freq[first] += 1

        return ans