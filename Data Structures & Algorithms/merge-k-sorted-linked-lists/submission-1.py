# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        # divide and conquer
        while len(lists) > 1:
            # merge every 2, if odd, then last one stays same.
            newList = []
            for i in range(0, len(lists), 2):
                if i + 1 >= len(lists):
                    newList.append(lists[i])
                else:
                    newList.append(self.mergeTwoLists(lists[i], lists[i+1]))
            lists = newList
        return lists[0]

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list2:
            cur.next = list2
        elif list1:
            cur.next = list1
        return dummy.next
            