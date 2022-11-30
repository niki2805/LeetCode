class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev1,prev2=0,0
        
        for i in nums:
            #print(prev1,prev2)
            prev1,prev2=prev2,max(prev1+i,prev2)
            
        return prev2
    