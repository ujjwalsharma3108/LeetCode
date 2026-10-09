class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        coll = {}
        ans = []
        for i in strs:
            j = "".join(sorted(i))
            if j in coll :
                coll[j].append(i)
            else:
                coll[j] = [i]
                
        for i,j in coll.items():
            ans.append(j)
        return ans