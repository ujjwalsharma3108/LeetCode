class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        dic = sorted(zip(position,speed),reverse=True)
        
        fleet = 0
        max_time = 0
        
        for pos,spd in dic:
            time = (target - pos) / spd
            if time > max_time:
                fleet+=1
                max_time = time

        return fleet
                
            
