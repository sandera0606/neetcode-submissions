# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find mid point
        mid, fast = head, head
        if not head:
            return
        
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next

        prev = mid
        mid = mid.next
        prev.next = None

        # 2. reverse second half
        two = self.reverseList(mid)

        # 3. merge lists
        self.mergeLists(head, two)
    
    def mergeLists(self, one, two):
        dummy = ListNode()
        cur = dummy
        while one and two:
            cur.next = one
            one = one.next
            cur.next.next = two
            two = two.next
            cur = cur.next.next
    
        cur.next = one or two
        return dummy.next

    def reverseList(self, node):
        cur, prev = node, None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev