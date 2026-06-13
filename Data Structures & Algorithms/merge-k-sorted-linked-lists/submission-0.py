import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy # cur.next <- deleteMin()
        # heapify pointers
        minHeap = []
        for head in lists:
            heapq.heappush(minHeap, NodeWrapper(head))
        
        # list that you deleted min from <- node.next. If None, remove that item from heap
        while minHeap:
            nxt = heapq.heappop(minHeap)
            cur.next = nxt.node
            if nxt.node.next:
                heapq.heappush(minHeap, NodeWrapper(nxt.node.next))
            cur = cur.next

        
        # return dummy.next
        return dummy.next