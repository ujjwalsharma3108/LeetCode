class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = format(n,'032b')
        new_str = bin_str[::-1]
        return int(new_str,2)