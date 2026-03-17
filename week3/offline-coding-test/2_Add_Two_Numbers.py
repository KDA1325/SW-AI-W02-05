# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        result = head

        sum = 0
        isOver10 = 0

        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + isOver10
        
            isOver10 = 0
        
            new_node = ListNode(sum % 10)
        
            if sum >= 10:
                isOver10 = 1

            result.next = new_node
            result = result.next

            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            sum = l1.val + isOver10
        
            isOver10 = 0
            
            if sum >= 10:
                isOver10 = 1

            new_node = ListNode(sum%10)

            result.next = new_node
            result = result.next

            l1 = l1.next

        while l2 is not None:
            sum = l2.val + isOver10
        
            isOver10 = 0
            
            if sum >= 10:
                isOver10 = 1

            new_node = ListNode(sum%10)

            result.next = new_node
            result = result.next
            
            l2 = l2.next

        if isOver10 == 1:
            new_node = ListNode(1)
            result.next = new_node

        return head.next 