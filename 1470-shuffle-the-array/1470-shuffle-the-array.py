class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        l,r=0,n
        while r!=len(nums):
            res.append(nums[l])
            l+=1
            res.append(nums[r])
            r+=1
        return res