class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
        for c in counts:
            if c != 0:
                return False
        return True

###Array: A data structure that stores elements in a contiguous block of memory, allowing for fast access and iteration.