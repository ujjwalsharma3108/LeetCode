class Solution(object):
    def gcdSum(self, nums):
        prefixGcd = []
        mx = 0

        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(self.getGcd(num, mx))
        prefixGcd.sort()  
        print(prefixGcd)
        
        s = 0
        e = len(prefixGcd) -1
        ret_sum  = 0
        while s < e  : 
            ret_sum += self.getGcd(prefixGcd[s],prefixGcd[e])
            s+=1
            e-=1
        return ret_sum

        

    def getGcd(self,a,b):
        while b != 0:
            a,b = b ,a%b
        return a
    
    def removeDuplicate(self,items):
        if not items:
            return []

        result = [items[0]]

        for num in items[1:]:
            if num != result[-1]:
                result.append(num)

        return result

