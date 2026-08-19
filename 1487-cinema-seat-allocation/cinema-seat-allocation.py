class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for row, seat in reservedSeats:
            rows.setdefault(row, []).append(seat)

        # Rows having no reservation can accommodate 2 families
        ans = (n - len(rows)) * 2

        for seats in rows.values():
            ans += self.countVacancy(seats)

        return ans

    def countVacancy(self, arr):
        reserved = set(arr)

        left = all(seat not in reserved for seat in [2, 3, 4, 5])
        middle = all(seat not in reserved for seat in [4, 5, 6, 7])
        right = all(seat not in reserved for seat in [6, 7, 8, 9])

        if left and right:
            return 2

        if left or middle or right:
            return 1

        return 0

        
            