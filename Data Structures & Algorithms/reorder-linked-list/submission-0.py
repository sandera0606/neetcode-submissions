# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        halfHead = None
        halfMark = math.ceil(self.listLength(head) / 2)

        cur = head

        for i in range(halfMark):
            if i == halfMark - 1:
                halfHead = cur
                break
            cur = cur.next
        
        reversedHalf = self.reverseList(halfHead)

        return self.mergeList(head, reversedHalf)

    def reverseList(self, head):
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev
    
    def mergeList(self, head1, head2):
        head = head1
    
        while head1 and head2:
            temp1 = head1.next
            head1.next = head2
            temp2 = head2.next
            head2.next = temp1

            head1 = temp1
            head2 = temp2

        return head1
    
    def listLength(self, head):
        length = 0

        while head:
            length += 1
            head = head.next
        
        return length
        
