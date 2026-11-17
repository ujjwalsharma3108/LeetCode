class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = format(n,'032b')
        return int(bin_str[::-1],2)