class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        x = sorted(zip(position,speed), reverse = True)
        print(x)
        count = 0
        arrivals = []
        for i in range(len(x)):
            
            eta= (target-x[i][0])/x[i][1]
            if len(arrivals)==0:
                arrivals.append(eta)
                count+=1
            else:
                if eta>arrivals[-1]:
                    count+=1
                    arrivals.append(eta)
        print(arrivals)
        return count
        
