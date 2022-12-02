class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums)
        
        if target % 2: return False # sum must be even number to divide it nums into 2 parts
        
        target //= 2
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        
        for r in range(len(nums) + 1):
            dp[r][0] = True # any array can form a target sum of 0
        
        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):
                t = c
                val = nums[r - 1]
                
                if t - val >= 0:
                    dp[r][c] = dp[r - 1][t - val]
                
                dp[r][c] = dp[r][c] or dp[r - 1][c]
                
                if t == target and dp[r][c]: return True
                
        return False
        
        def subsetSumToK(n, k, arr):
            dp = [[False for i in range(k+1)] for j in range(n+1)]
            for i in range(n):
                dp[i][0]=True
            for ind in range(1,n):
                for target in range(1,k+1):
                    not_take=dp[ind-1][target]
                    take=False
                    if arr[ind]<=target:
                        take=dp[ind-1][target-arr[ind]]
                    dp[ind][target]=take or not_take
            #print(dp)
            return dp[n-1][k]
        n=len(nums)
        total_sum=sum(nums)
        target=total_sum//2
        if total_sum%2!=0:
            return False
        return subsetSumToK(n, target, nums)
        