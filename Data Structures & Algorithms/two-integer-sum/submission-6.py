class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        """
        Nested Loops
        O(n2) O(1)
        """

        # for i in range(n - 1): 
        #     for j in range(i  + 1, n): 
        #         if nums[i] + nums[j] == target: 
        #             return [i, j]

        # return [-1, -1]

        """
        Using Dictionary
        """
        dct = {}

        for i in range(n):
            diff = target - nums[i] 
            if diff in dct: 
                return [dct[diff], i]
            dct[nums[i]] = i

        return [-1, -1]
        