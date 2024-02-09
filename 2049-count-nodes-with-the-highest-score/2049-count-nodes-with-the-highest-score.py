class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        graph = collections.defaultdict(list)
        
        for node, parent in enumerate(parents):  # build graph
            graph[parent].append(node)
        # {-1: [0], 2: [1, 3], 0: [2, 4]}
        n = len(parents)                         # total number of nodes
        d = collections.Counter()
        
        
        def countNodes(node):                    # number of children node + self
            p, s = 1, 0                          # p: product, s: sum
            for child in graph[node]:            # for each child (only 2 at maximum)
                res = countNodes(child)          # get its nodes count
                p *= res                         # take the product
                s += res                         # take the sum
            p *= max(1, n - 1 - s)               # times up-branch (number of nodes other than left, right children ans itself)
            d[p] += 1                            # count the product
            return s + 1 
        
        countNodes(0)                            # starting from root (0)
        return d[max(d.keys())]                  # return max count
        """
            {-1: [0], 2: [1, 3], 0: [2, 4]}
            countNodes(0)
            
            Root
            p, s = 1, 0
            2
            res = countNodes(2)
            
                Node 2
                p, s = 1, 0
                
                Node 1
                res = countNodes(1)
    
                    p, s = 1, 0
                    p = 3 - 1 - 0 = 2*1 = 2
                    d[2] += 1
                    return 1
                    
                res = 1
                p = 1*1 = 1
                s += 1 # s = 1

                Node 3
                res = countNodes(3)
                    
                    p, s = 1, 0
                    p = 3 - 1 - 0 = 2*1 = 2
                    d[2] += 1
                    return 1
                    
                res = 1
                p = 1*1 = 1
                s += 1 # s = 2
            
                p = 3 - 1 - 2 = max(1, 0) = 1*1 = 1
                d[1] += 1      
                return 2 + 1 = 3
                
            res = 3
            p = 3 * 1 = 3
            s += 3 # s = 3
            
            Node 4
            res = countNodes(4)
        
                    p, s = 1, 0
                    p = 3 - 1 - 0 = 2*1 = 2
                    d[2] += 1 # {1: 1, 2: 3}
                    return 1
            
            res = 1
            p = 3 * 1 = 3
            s += 1 # s = 4
            p = 3 - 1 - 4 = max(1, -4) = 1
            d[1] += 1 # {1: 2, 2: 3}
            return 2 + 1 = 3
            
            
            return d[max(d.keys())] 
            
            
        
        """