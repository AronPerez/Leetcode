# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False  # Empty list or single node, no cycle
    
        tortoise = head  # Slower pointer
        hare = head.next  # Faster pointer

        while tortoise != hare:
            if hare is None or hare.next is None:
                return False  # Reached the end, no cycle
            tortoise = tortoise.next
            hare = hare.next.next

        # If the loop exits, there is a cycle
        return True
        