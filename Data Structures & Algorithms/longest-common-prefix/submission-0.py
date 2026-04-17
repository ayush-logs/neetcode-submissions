class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Most Naive Solution? 

        """

        """
        Sort & Compare first and last strings
        """
        # Sorting the array
        strs.sort()

        first = strs[0]
        last = strs[-1]

        i = 0

        while i < len(first) and first[i] == last[i]: 
            i += 1

        return first[:i]
        