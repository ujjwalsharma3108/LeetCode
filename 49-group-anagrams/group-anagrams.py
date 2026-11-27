class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        coll = {}
        for i in strs :
            ss = "".join(sorted(list(i)))
            if ss in coll:
                coll[ss].append(i)
            else:
                coll[ss] = [i]
        return [j for i , j in coll.items() ]