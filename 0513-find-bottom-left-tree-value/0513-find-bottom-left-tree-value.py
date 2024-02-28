# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxDepth = -1
        bottomLeftValue = 0

        def dfs(current: TreeNode, depth: int):
            nonlocal bottomLeftValue
            nonlocal maxDepth
            if not current:
                return

            if depth > maxDepth:  # If true, we discovered a new level
                maxDepth = depth
                bottomLeftValue = current.val

            dfs(current.left, depth + 1)
            dfs(current.right, depth + 1)
            return
        
        dfs(root, 0)
        return bottomLeftValue