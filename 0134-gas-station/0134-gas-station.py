class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start,tank,cur=0,0,0
        
        for i in range(len(gas)):
            tank+=gas[i]-cost[i]
  
            cur+=gas[i]-cost[i]
            if cur<0:
                start=i+1
                cur=0
        #print(tank)       
        return start if tank>=0 else -1
        
        