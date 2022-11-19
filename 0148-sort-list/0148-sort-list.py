# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        left=head
        right=self.getmid(left)
        
        temp=right.next
        right.next=None
        right=temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.mergeLists(left, right)
        
                               
    def getmid(self,head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def mergeLists(self, list1, list2):
        tail = dummy = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2
            
        return dummy.next
            