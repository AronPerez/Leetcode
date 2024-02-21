class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize pointers and variables
        i = j = 0
        n, m = len(word1), len(word2)

        # Create a new string to store the merged string
        merged = ""

        # Iterate over both strings simultaneously
        while i < n and j < m:
            # Append the i-th character of word1 to the merged string
            merged += word1[i]

            # Append the j-th character of word2 to the merged string
            merged += word2[j]

            # Increment both pointers
            i += 1
            j += 1

        # Append the remaining characters of the longer string to the merged string
        if i < n:
            merged += word1[i:]
        if j < m:
            merged += word2[j:]

        # Return the merged string
        return merged

        