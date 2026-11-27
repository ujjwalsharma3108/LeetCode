class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        coll = defaultdict(list)
        for s in strs:
            coll["".join(sorted(s))].append(s)
        return list(coll.values())