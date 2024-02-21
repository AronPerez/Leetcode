# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')  # Initialize with negative infinity

        def dfs(node):
            nonlocal result  # Allow modification of the outer 'result'

            if not node:
                return 0

            left = max(0, dfs(node.left))   # Max gain from the left subtree
            right = max(0, dfs(node.right))  # Max gain from the right subtree

            # Update the max path sum if including the current node is better
            result = max(result, node.val + left + right) 

            # Return maximum gain achievable if extending the path from this node
            return node.val + max(left, right)

        dfs(root)
        return result
        