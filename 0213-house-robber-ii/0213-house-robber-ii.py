class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
 
            prev1,prev2=0,0
        
            for i in range(len(nums)):
           
                prev1,prev2=prev2,max(prev1+nums[i],prev2)
            
     
            return prev2
            
 
        
        
        return max(nums[0]+helper(nums[2:-1]),helper(nums[1:]))
                
        