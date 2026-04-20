class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n  = len(nums)

        # check for zero count - O(n)
        zero_count = 0 
        for num in nums: 
            if num == 0: 
                zero_count += 1
        
        if zero_count > 1: 
            return [0] * n

        # nested loop
        res = [1] * n
        for i in range(n): 
            for j in range(n) :
                if i != j: 
                    res[i] *= nums[j] 

        
        return res
                    
