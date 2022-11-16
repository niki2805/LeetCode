class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans=[0]*len(T)
        stack=[]
        
        for i in range(len(T)):
            
            while stack and T[i]>T[stack[-1]]:
                ans[stack[-1]]=i-stack[-1]
                stack.pop()
                
            stack.append(i)
            
        return ans
        