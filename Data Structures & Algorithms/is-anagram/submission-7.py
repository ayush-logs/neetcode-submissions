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
            O(n) O(d) :: d is number of distinct characters
        """
        # return Counter(s) == Counter(t)

        """
            Default Dictionary - For Lower Case Letters Only 
        """
        # dct1 = defaultdict(int)
        # dct2 = defaultdict(int)

        # for char in s: 
        #     dct1[char] += 1

        # for char in t: 
        #     dct2[char] += 1
        
        # return dct1 == dct2

        """
        Array Based Frequency Counter - Lower Case Letters Only
        """
        lst  = [0] * 26
        for char in s: 
            lst[ ord(char) - ord('a')] += 1
        
        for char in t: 
            lst[ord(char) - ord('a')] -= 1

        return all(x == 0 for x in lst)


        

        
        