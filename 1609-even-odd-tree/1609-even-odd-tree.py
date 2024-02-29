# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # Goes even, odd, even odd
        
        queue = deque([root])
        isEven = True
        
        while queue:
            queueLen = len(queue)
            prevValue = float('inf')
            
            if isEven:
                prevValue = float('-inf')
            
            for i in range(queueLen):
                currentNode = queue.popleft() 
      
                # Going left to right when even
                # Ensure the current nodes value is less than prev

                # Going left to right when odd
                # Ensure the current nodes value is more than prev
                if (isEven and (currentNode.val % 2 == 0 or currentNode.val <= prevValue)) or \
                (not isEven and (currentNode.val % 2 == 1 or currentNode.val >= prevValue)):
                    return False
            
                prevValue = currentNode.val
                # Put next vals in
                if currentNode.left:
                    queue.append(currentNode.left)
                    
                if currentNode.right:
                    queue.append(currentNode.right)
                
                    
            isEven = not isEven
            
        return True