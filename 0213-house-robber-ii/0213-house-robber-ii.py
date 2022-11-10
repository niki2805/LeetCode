class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solve(start,end):
            one,two=0,0
            for i in range(start,end+1):
                one,two=max(one,two+nums[i]),one
                
            return one
        
        n = len(nums)
        if n == 1: return nums[0]
        
        return max(solve(0, n-2), solve(1, n-1))
                
        