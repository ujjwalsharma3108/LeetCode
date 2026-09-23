class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        last = 0
        def reoccurTask(arr,present,count):
            if count == n -1:
                return 
            c = 0
            while c != k :
                present = present % n
                if arr[present] == -1:
                    present +=1
                    continue
                c+=1
                present+=1
            present = present % n 
            arr[present-1] = -1
            last = present-1
            count+=1
            reoccurTask(arr,present,count)
        reoccurTask(arr,0,0)

        for i in arr:
            if i != -1:
                return i
        

        