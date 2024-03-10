# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        # Initialize the curr pointer to the dummy node
        curr = dummy

        # Traverse the linked list using the curr pointer
        while curr.next:
            # If the current node and the next node have the same value
            if curr.next.next and curr.next.val == curr.next.next.val:
                # Store the duplicate value
                duplicate_val = curr.next.val

                # Skip all duplicate nodes with the same value
                while curr.next and curr.next.val == duplicate_val:
                    curr.next = curr.next.next
            # If the current node and the next node have different values
            else:
                # Move curr one step forward
                curr = curr.next

        # Return the modified linked list (excluding the dummy node)
        return dummy.next