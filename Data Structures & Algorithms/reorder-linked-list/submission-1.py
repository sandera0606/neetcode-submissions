# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        halfLen = math.ceil(length / 2)
        cur = head
        prev = None
        for i in range(halfLen):
            prev = cur
            cur = cur.next
        prev.next = None
        list2 = self.reverseList(cur)

        self.mergeLists(head, list2)
        
    def reverseList(self, start: Optional[ListNode]) -> ListNode:
        prev = None
        cur = start
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def mergeLists(self, list1, list2):
        # cur = list1
        # first = []
        # while cur:
        #     first.append(cur.val)
        #     cur = cur.next
        # cur = list2
        # second = []
        # while cur:
        #     second.append(cur.val)
        #     cur = cur.next
        # print("list 1 ", first)
        # print("list 2 ", second)
        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2
        