class Solution:
    def decodeString(self, s: str) -> str:

        def solve(i):
            result = ""
            number = 0

            while i < len(s):

                if s[i].isdigit():
                    number = number * 10 + int(s[i])
                    i += 1

                elif s[i].isalpha():
                    result += s[i]
                    i += 1

                elif s[i] == '[':
                    inner, i = solve(i + 1)
                    result += inner * number
                    number = 0

                else:  # ']'
                    return result, i + 1

            return result, i

        return solve(0)[0]