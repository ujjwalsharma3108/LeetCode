class Solution(object):
    def convertToTitle(self, columnNumber):
        result = []
        while columnNumber > 0:
            columnNumber -= 1  # Shift to 0-indexed for modulo arithmetic
            remainder = columnNumber % 26
            result.append(chr(65 + remainder))  # 65 is the ASCII value for 'A'
            columnNumber //= 26
        return "".join(reversed(result))
        