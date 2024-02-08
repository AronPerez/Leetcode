# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        
        queue = deque([root]) # TreeNode(val = 4, left=TreeNode(2..), right=TreeNode(7)
	
        while queue:
            currentNode = queue.popleft() # TreeNode(4..), TreeNode(7), TreeNode(2)
            # We swap left and right
            # left=TreeNode(2..), right=TreeNode(7) = left=TreeNode(7), right=TreeNode(2..)
            # left=TreeNode(6..), right=TreeNode(9) = left=TreeNode(9), right=TreeNode(6..)	
            # left=TreeNode(1..), right=TreeNode(3) = left=TreeNode(3), right=TreeNode(1..)

            currentNode.left, currentNode.right = currentNode.right, currentNode.left

            if currentNode.left:
                queue.append(currentNode.left) 
            # queue=[TreeNode(7)]/ queue=[TreeNode(2), TreeNode(9)]

            if currentNode.right:
                queue.append(currentNode.right) # queue=[TreeNode(7), TreeNode(2..)]
                # queue=[TreeNode(7)]/ queue=[TreeNode(2), TreeNode(9), TreeNode(6)]

        return root

        