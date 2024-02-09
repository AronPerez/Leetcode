class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tree = defaultdict(list)                # Create an empty dict of lists representing the tree structure
        for i, x in enumerate(parents):         # Iterate through parent-child relationships
            tree[x].append(i)                   # Add child nodes to their parent in the tree list
                
        freq = defaultdict(int)                 # Create a dictionary to store node score frequencies
        
        def fn(x):                              # Recursive function to calculate node score and frequency
            left = right = 0                    # Initialize left and right subtree sizes

            if tree[x]:                         # Call recursively for left child if it exists
                left = fn(tree[x][0])
                
            if len(tree[x]) > 1:                # Call recursively for right child if it exists
                right = fn(tree[x][1])
            
            score = (left or 1) * (right or 1) * (len(parents) - 1 - left - right or 1) # Calculate node score
            freq[score] += 1                    # Update frequency of the calculated score
            
            return 1 + left + right             # Return total subtree size (including current node)
        
        fn(0)                                   # Start calculation from the root node (0)
        return freq[max(freq)]                  # Return the frequency of the highest score