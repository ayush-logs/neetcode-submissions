class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        st = set()
        res = 0

        for right in range(len(s)): 
            while s[right] in st: 
                st.remove(s[left])
                left += 1
            
            st.add(s[right])
            res = max(res, right - left + 1)
        
        return res
            



        