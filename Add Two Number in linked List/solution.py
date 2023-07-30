## Link: https://leetcode.com/problems/add-two-numbers/description/?envType=featured-list&envId=top-interview-questions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        curr = head = None
    

        while(l1 or l2):
            if l1 and l2:
                combine = l1.val+l2.val+carry
                l1=l1.next
                l2=l2.next
            elif l1:
                combine = l1.val+carry
                l1=l1.next
            else:
                combine = l2.val+carry
                l2=l2.next

            if combine > 9:
                carry = 1
                combine = combine - 10
            else:
                carry = 0
            
            if curr:
                curr.next = ListNode(combine)
                curr = curr.next
            else:
                curr = ListNode(combine)
                head = curr
        
        if carry == 1:
            curr.next = ListNode(1)

        return head