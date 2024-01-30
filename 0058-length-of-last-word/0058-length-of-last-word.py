class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sArr = s.split()
        return len(sArr[len(sArr)-1])
        