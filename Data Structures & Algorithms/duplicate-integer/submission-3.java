class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        // Array is sorted
        Arrays.sort(nums);

        // Compare adjacent elements
        for(int i = 1; i < nums.length; i++){
            if(nums[i] - nums[i-1] == 0) return true; 
        } 

        return false; 

    }
}