# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
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