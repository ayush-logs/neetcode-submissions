class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0

        # find how many characters of t appear in s
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        
        res = len(t) - j

        return max(res, 0)
            
        