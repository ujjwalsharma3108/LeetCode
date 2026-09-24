class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        partition = []

        def isPalindrome(s):
            if len(s) == 1:
                return True

            for i in range(len(s)//2):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True

        def getAllParts(st,partition,ans):
            if(len(st) == 0):
                ans.append(partition.copy())
                return
            
            for i in range(len(st)):
                str_part = st[:i+1]

                if isPalindrome(str_part):
                    partition.append(str_part)
                    getAllParts(st[i+1:],partition,ans)
                    partition.pop()
        getAllParts(s,partition,ans)
        return ans

        

