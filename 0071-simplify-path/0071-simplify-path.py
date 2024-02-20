class Solution:
    def simplifyPath(self, path: str) -> str:
        # Delimit based on /
        # If it ends with a /, we can remove it since we dont care about it
        stack = []

        
        #W for value in stack:
        
        # Go through the stack and if you see a '', you know its a /
        
        # We can to reconstruct the ans using "".join(ans)
        # ans[-1] cannot be a /, if it is we can remove it
        for component in path.split('/'):
            if component == '..':
                if stack:
                    stack.pop()
            elif component == '.' or not component:
                continue
            else:
                stack.append(component)

        return '/' + '/'.join(stack)
                
                
        
                
  
            
        