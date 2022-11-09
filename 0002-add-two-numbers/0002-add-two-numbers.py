# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        s1,s2=1,1
        carry=0
        sums=temp=ListNode(0)
        
        while l1 or l2:
            num1,num2=0,0
            
            if l1:
                num1=l1.val
                l1=l1.next
            
            if l2:
                num2=l2.val
                l2=l2.next
            
            colsum=num1+num2+carry
            carry=colsum//10
            
            temp.next=ListNode(colsum%10)
            temp=temp.next
          
        if carry==1:
            temp.next=ListNode(val=1)
        return sums.next
        