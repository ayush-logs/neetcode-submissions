class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        """
            Sort & Compare Approach
            O(nlogn) O(n)
        """
        # return sorted(s) == sorted(t)

        """
            Counter DS
        """
        return Counter(s) == Counter(t)
        """
            List Counter - For Lower Case Letters Only 
        """



        

        
        