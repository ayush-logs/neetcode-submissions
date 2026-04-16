class Solution {
    public int maxArea(int[] nums) {
        int l = 0, r = nums.length - 1; 
        int max = 0; 

        while(l < r){
            int height = Math.min(nums[l], nums[r]); 
            int currVol = height * (r - l);
            max = Math.max(currVol, max); 
            if(nums[l] < nums[r]) l++; 
            else r--; 
        }

        return max; 
    }
}
