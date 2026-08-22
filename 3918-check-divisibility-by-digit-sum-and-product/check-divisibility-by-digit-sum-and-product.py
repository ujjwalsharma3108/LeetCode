class Solution:
    def checkDivisibility(self, n: int) -> bool:
        multi = 1
        sub = 0
        number = n
        while number > 0:
            digit = number % 10
            multi *= digit
            sub += digit
            number = number//10
        return n % (multi + sub) == 0