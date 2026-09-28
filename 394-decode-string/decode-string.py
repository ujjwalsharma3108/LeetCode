class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)

            else:
                # 1. Closing bracket tak string nikalo
                temp = ""

                while stack[-1] != '[':
                    temp = stack.pop() + temp

                stack.pop()  # '[' remove

                # 2. Number nikalo
                num = ""

                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                # 3. Repeat k times
                decoded = temp * int(num)

                # 4. Wapas stack me daal do
                stack.append(decoded)

        return ''.join(stack)