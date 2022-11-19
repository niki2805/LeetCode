# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy_start = ListNode(None)
        dummy_start.next=head
        head = dummy_start
  
        i = 0
        node = head
        while i < left - 1:
            node = node.next
            i += 1
        before_left = node 
            
 
        while i < right:
            node = node.next
            i += 1
        before_right = node 
        after_right = before_right.next
        
     
        prev, curr = after_right, before_left.next  
        while curr is not None and curr != after_right:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
           
        before_left.next = prev
        

        return head.next