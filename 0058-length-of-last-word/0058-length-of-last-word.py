class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        result = s.split()
        return len(result[-1])
        