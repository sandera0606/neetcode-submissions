# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        encountered_nodes = set()
        cur_node = head
        while cur_node:
            if cur_node in encountered_nodes:
                return True
            else:
                encountered_nodes.add(cur_node)
            cur_node = cur_node.next

        return False