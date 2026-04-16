class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nested loop approach 
        # O(n2) O(1)

        n: int = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n): 
                if nums[i] == nums[j]:
                    return True

        return False