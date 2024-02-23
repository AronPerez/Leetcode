# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, max_so_far):
            if not node:
                return 0

            good_nodes = 0
            if node.val >= max_so_far:
                good_nodes += 1
                max_so_far = node.val

            good_nodes += dfs(node.left, max_so_far)
            good_nodes += dfs(node.right, max_so_far)

            return good_nodes

        return dfs(root, float('-inf'))
        