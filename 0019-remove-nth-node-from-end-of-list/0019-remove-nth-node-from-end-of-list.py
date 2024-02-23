# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of a linked list.

        Args:
        head: The head of the linked list.
        n: The number of nodes to remove from the end of the list.

        Returns:
        The head of the linked list after removing the nth node.

        Example:
        >>> remove_nth_node_from_end([1, 2, 3, 4, 5], 2)
        [1, 2, 3, 5]
        """

        # Check if the input is valid.
        if not head or n <= 0:
            raise ValueError("Invalid input.")

        # Find the length of the linked list.
        length = 0
        current_node = head
        while current_node:
            length += 1
            current_node = current_node.next

        # Calculate the index of the node to remove.
        index_to_remove = length - n

        # If the node to remove is the head of the list, return the next node.
        if index_to_remove == 0:
            return head.next

        # Otherwise, traverse the list and remove the node.
        current_node = head
        previous_node = None
        for i in range(index_to_remove):
            previous_node = current_node
            current_node = current_node.next

        # Update the previous node's next pointer to skip the node to remove.
        previous_node.next = current_node.next

        # Return the head of the linked list.
        return head
        