class Solution:
    def simplifyPath(self, path: str) -> str:
        # Delimit based on /
        # If it ends with a /, we can remove it since we dont care about it
        stack = []
        components = path.split('/')
        for component in components:
            if component == '.' or component == '':
                continue
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)
        return '/' + '/'.join(stack)
                
                
        
                
  
            
        