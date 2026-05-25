# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.lengthList(head)
        N = length - n

        if N == 0:
            return head.next
        
        i = 0
        cur = head
        while i < N - 1:
            i += 1
            cur = cur.next
        
        if cur.next:
            cur.next = cur.next.next
        
        return head

    def lengthList(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length