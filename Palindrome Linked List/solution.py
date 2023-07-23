# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        queue = []
        even = False
        if not head:
            return False
        
        curr = head
        fast = head

        while(fast != None and fast.next!=None):

            queue.append(curr.val)
            curr = curr.next

            if fast.next.next:
                fast = fast.next.next
            else:
                even = True
                break
        mid = curr
        if not even :
            mid = curr.next
        
        #print(queue,mid.val)
        palindrome = True
        while(len(queue)>0 or mid):
            last = queue.pop()
            if last != mid.val:
                palindrome = False
                break
            mid = mid.next
        return palindrome