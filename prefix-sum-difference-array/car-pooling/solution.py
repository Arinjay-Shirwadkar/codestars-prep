class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    
        dif= [0]*1001
        
        for passengers,start,end in trips:
            dif[start] += passengers
            dif[end] -= passengers  
            
        passengers = 0
        for count in dif:
            passengers += count
            if passengers> capacity:
                return False
                
        return True