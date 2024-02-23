# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        global_max_sum = float('-inf')

        def find_max_path_sum(root):
            nonlocal global_max_sum
            if root is None:
                return 0

            left_max_path_sum = find_max_path_sum(root.left)
            right_max_path_sum = find_max_path_sum(root.right)

            max_path_sum = max(root.val, root.val + left_max_path_sum, root.val + right_max_path_sum, root.val + left_max_path_sum + right_max_path_sum)
            global_max_sum = max(global_max_sum, max_path_sum)

            return max(root.val, root.val + max(left_max_path_sum, right_max_path_sum))

        find_max_path_sum(root)

        return global_max_sum

        