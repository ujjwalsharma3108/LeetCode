class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        coll = {}
        for i in nums:
            if i in coll:
                coll[i] +=1
            else:
                coll[i] = 1

        new_list = sorted(coll.values(),reverse=True)[:k]
        print(new_list)

        return [i  for i , j in coll.items() if j in new_list]
        

        