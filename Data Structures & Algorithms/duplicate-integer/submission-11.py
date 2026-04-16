class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # early exit
        
        st = set()

        for num in nums: 
            if num in st: 
                return True
            st.add(num)

        return False