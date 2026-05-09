class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        # char count map of s2
        s1_count = Counter(s1)

        # char count map for s1
        window_count  = Counter(s2[:k])

        if s1_count == window_count: 
            return True

        l = 0

        for r in range(k, len(s2)): 
            window_count[s2[r]] = 1 + window_count.get(s2[r], 0)

            char_out = s2[l]
            window_count[char_out]  -= 1

            if window_count[char_out] == 0: 
                del window_count[char_out]
            
            l += 1

            if window_count == s1_count: 
                return True

            
        return False



        