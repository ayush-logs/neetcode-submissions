class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        l = 0
        count  = {} 
        maxf = 0

        for r in range(len(s)): 
            # add the character to the hashmap
            count[s[r]] = 1 + count.get(s[r], 0)

            # update maxf
            maxf = max(count[s[r]], maxf)

            # update when distinct character count exceeds k
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max((r - l + 1), res)

        
        return res

        
        