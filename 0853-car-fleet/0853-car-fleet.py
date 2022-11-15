class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [car for car in zip(position, speed)]
        
        cars.sort(key=lambda car: -car[0])
        
        stack=[]
        for pos,sp in cars:
            time=(target-pos)/sp
            
            if not stack or time>stack[-1]:
                stack.append(time)
                
        return len(stack)
       
        