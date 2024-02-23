class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        simplified_path = ""

        for directory in path.split("/"):
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory != "." and directory != "":
                stack.append(directory)

        simplified_path = "/" + "/".join(stack)

        return simplified_path