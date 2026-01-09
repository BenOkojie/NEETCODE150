# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        start = list1
        if list1.val<=list2.val:
            list1=list1.next
        else:
            start= list2
            list2 = list2.next
        head = start
        while head:
            if list1 and list2:
                if list1.val<=list2.val:
                    head.next = list1
                    head = head.next
                    list1=list1.next
                else:
                    head.next= list2
                    head = head.next
                    list2 = list2.next
            elif list1 and not list2:
                head.next=list1
                return start
            elif list2 and not list1:
                head.next=list2
                return start
        return start
                
            
