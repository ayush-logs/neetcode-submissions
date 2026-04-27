class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p  = 1
        i = 1
        while i < len(nums): 
            if nums[i] != nums[i - 1]: 
                nums[p] = nums[i]
                p += 1
            i += 1
        
        return p
        