# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')

        def dfs(node):
            nonlocal max_path_sum
            
            if not node:
                return 0

            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))

            max_path_sum = max(max_path_sum, node.val + left_max + right_max)

            return node.val + max(left_max, right_max)

        dfs(root)

        return max_path_sum


        