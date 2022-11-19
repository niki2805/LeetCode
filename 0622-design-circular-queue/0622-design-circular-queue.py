class ListNode:
    def __init__(self,val,next=None):
        
        self.val=val
        self.next= next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.count=0
        self.front=None
        self.rear=None
             
    def enQueue(self, value: int) -> bool:
  
        
        if self.isFull():
            return False
        
        if  self.front is None:
            self.rear = self.front = ListNode(value)
            self.count += 1
            
            return True
        
        self.rear.next = ListNode(value)
        self.rear = self.rear.next
        self.count += 1
        return True
                  
    def deQueue(self) -> bool:
        
        if self.isEmpty():
            return False

        self.front = self.front.next
        self.count -= 1
        
        return True
        

    def Front(self) -> int:
        if (self.isEmpty()):
            return -1
        return self.front.val
        
    def Rear(self) -> int:
        if self.isEmpty():
            
            return -1
        return self.rear.val
        

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()