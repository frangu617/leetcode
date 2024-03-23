# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()  # Dummy head of the result linked list
        current = dummy_head      # Pointer to the current node in the result linked list
        carry = 0                 # Variable to store the carryover
        
        while l1 or l2 or carry:
            # Calculate the sum of current digits and carryover
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            # Update carryover and create a new node for the result
            carry, digit = divmod(sum_val, 10)
            current.next = ListNode(digit)
            current = current.next
        
        return dummy_head.next