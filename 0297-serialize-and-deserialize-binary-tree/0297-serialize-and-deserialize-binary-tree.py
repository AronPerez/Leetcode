# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Base case: if root is None, return empty string
        if not root:
            return ""

        # Create a queue for BFS traversal and add root to it
        queue = [root]
        result = []

        # Perform BFS traversal
        while queue:
            node = queue.pop(0)

            # If node is None, append "None" to result
            if not node:
                result.append("None")
            else:
                # Append node value to result and add its left and right children to the queue
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        # Join the result list into a string and return it
        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Base case: if data is empty, return None
        if not data:
            return None

        # Split the data string into a list of values
        values = data.split(",")
        
        # Create the root node using the first value
        root = TreeNode(int(values[0]))
        
        # Create a queue for BFS traversal and add root to it
        queue = [root]
        index = 1

        # Perform BFS traversal
        while queue:
            node = queue.pop(0)

            # If the current value is not "None", create a left child node
            if values[index] != "None":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1

            # If the current value is not "None", create a right child node
            if values[index] != "None":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1

        # Return the deserialized binary tree
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))