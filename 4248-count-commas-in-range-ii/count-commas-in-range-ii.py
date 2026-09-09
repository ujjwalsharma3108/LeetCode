class Solution(object):
    def countCommas(self, n):
        i = 3
        count = 0
        while n > (10**i -1):
            count += n - (10**i - 1)
            i += 3

        return count
        