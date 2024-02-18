class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the array is empty, return an empty string.
        if not strs:
            return ""

        # Initialize the longest common prefix string.
        longest_common_prefix = ""
        # Find the shortest string in the array.
        shortest_str = min(strs, key=len)

        # Iterate over the characters in the shortest string.
        for i in range(len(shortest_str)):
            # Check if all the strings in the array have the same character at the current index.
            char = shortest_str[i]
            if all(s[i] == char for s in strs):
                # If all the strings have the same character, add it to the longest common prefix string.
                longest_common_prefix += char
            else:
                # If not all the strings have the same character, return the longest common prefix string so far.
                return longest_common_prefix

        # Return the longest common prefix string.
        return longest_common_prefix
        