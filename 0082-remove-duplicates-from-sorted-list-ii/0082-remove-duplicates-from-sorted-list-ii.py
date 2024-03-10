# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle the case where the head node needs to be deleted
        dummy = ListNode(0)
        dummy.next = head

        # Initialize the prev pointer to the dummy node
        prev = dummy

        # Traverse the linked list using the head pointer
        while head:
            # Skip all duplicate nodes with the same value as the current node
            while head.next and head.val == head.next.val:
                head = head.next

            # If prev.next is not the same as head, it means there were duplicates
            # Update prev.next to skip the duplicates and point to the next distinct node
            if prev.next != head:
                prev.next = head.next
            # If prev.next is the same as head, it means there were no duplicates
            # Move prev one step forward
            else:
                prev = prev.next

            # Move head one step forward
            head = head.next

        # Return the modified linked list (excluding the dummy node)
        return dummy.next