# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        last_node = None

        carry = 0
        curr_val = 0
        while True:
            if l1 is None and l2 is None:
                break

            if l1 is not None:
                curr_val += l1.val
                l1 = l1.next
            
            if l2 is not None:
                curr_val += l2.val
                l2 = l2.next
            
            if curr_val >= 10:
                curr_val %= 10
                carry = 1
            
            newnode = ListNode(curr_val)
            if result is None:
                result = newnode
                last_node = newnode
            else:
                last_node.next = newnode
                last_node = newnode

            curr_val = carry
            carry = 0

        if curr_val != 0:
            last_node.next = ListNode(curr_val)
        return result

        