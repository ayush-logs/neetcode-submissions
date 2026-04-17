class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_lst = []

        for num in nums: 
            if num != val: 
                new_lst.append(num)

        for i in range(len(new_lst)): 
            nums[i] = new_lst[i]

        return len(new_lst)
        