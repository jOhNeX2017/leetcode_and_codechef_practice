<!-- https://leetcode.com/problems/merge-two-sorted-lists -->

# Intuition
Go through each node of list1 and list2 and compare the value of the node 
whichever is smaller add it to the head

# Approach
Simply traverse the lists and add the value whenever we get the samllest number.

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$
# Code
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 and list2:
            newList = None

            if list1.val < list2.val :
                newList = ListNode(list1.val)
                list1 = list1.next
            else:
                newList = ListNode(list2.val)
                list2 = list2.next

            head = newList

            while (list1 and list2) :
                if list1.val < list2.val :
                    # addtoList(list1)
                    head.next = list1
                    list1 = list1.next
                    head = head.next
                else:
                    # addtoList(list2)
                    head.next = list2
                    list2 = list2.next
                    head = head.next
            
            if list1:
                head.next = list1

            if list2:
                head.next = list2

            return newList
        else:
            return list1 if list1 else list2


```

The Second solution is same just the lines of code is less & more optimesed as well.