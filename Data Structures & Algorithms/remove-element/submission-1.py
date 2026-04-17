class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        """
        O(n) O(n)
        """
        # new_lst = []

        # for num in nums: 
        #     if num != val: 
        #         new_lst.append(num)

        # for i in range(len(new_lst)): 
        #     nums[i] = new_lst[i]

        # return len(new_lst)

        l = 0 # point to the last occurence of val? 

        for i in range(len(nums)): 
            if nums[i] != val:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1

        return l
                
        