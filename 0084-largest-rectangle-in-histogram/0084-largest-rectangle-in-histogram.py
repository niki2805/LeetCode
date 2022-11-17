class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
       
        stack=[]
        heights.append(0)
        ans=0
        
        for i,h in enumerate(heights):

            while stack and heights[stack[-1]]>=h:
             
                H=heights[stack.pop()]
                W=i if not stack else i-1-stack[-1]
                ans=max(ans,H*W)
      
            stack.append(i)
            
        return ans
            
           
            
        