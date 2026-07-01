# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            mergedLists = []
            i = 0
            while i < len(lists):
                if i + 1 < len(lists):
                    mergedLists.append(self.merge2Lists(lists[i], lists[i+1]))
                else:
                    mergedLists.append(lists[i])
                i += 2
            lists = mergedLists

        return lists[0]
        
    def merge2Lists(self, list1, list2):
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
        
        cur.next = list1 or list2

        return dummy.next