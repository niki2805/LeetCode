class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        
        for i in operations:
            if i=='C':
                stack.pop()
            elif i=='D':
                a=stack[-1]
                stack.append(2*a)
            elif i=='+':
                a,b=stack[-1],stack[-2]
                stack.append(a+b)
            else:
                stack.append(int(i))
                
        return sum(stack)
        