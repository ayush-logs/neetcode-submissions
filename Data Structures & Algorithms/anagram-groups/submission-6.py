class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        Check for anagram by sorting
        O(m * n) O (m * n)
        """
        # res = defaultdict(list)

        # for s in strs: 
        #     key = "".join(sorted(s))
        #     res[key].append(s)

        # return list(res.values())
        
        """
        2nd way of checking for anagram, using char freq array
        """

        res = defaultdict(list)

        for s in strs: 
            count = [0] * 26
            for c in s: 
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())