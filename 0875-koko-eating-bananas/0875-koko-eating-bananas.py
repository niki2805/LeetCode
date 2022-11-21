import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def bs(k):
            total=0
            for i in piles:
                total+=math.ceil(i/k)
               
             
            return total
    
    
        l,r=1,max(piles)
        
        while(l<r):
            mid=(l+r)//2
         
            if bs(mid) <= h:
                r=mid
            else:
                l=mid+1
                
        return l