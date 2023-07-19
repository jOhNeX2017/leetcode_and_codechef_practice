
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_node(prev,curr,next):
            if not next:
                return curr
            
            prev = curr
            curr = next
            next = next.next

            curr.next = prev

            return reverse_node(prev,curr,next)

        if head:
            temp = head
            new_head = reverse_node(None,head,head.next)
            temp.next = None
            return new_head
        else:
            return head
