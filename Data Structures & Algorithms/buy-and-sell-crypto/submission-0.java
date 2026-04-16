class Solution {
    public int maxProfit(int[] nums) {
        // profit = selling - buying
        int max = 0, bp = nums[0]; 

        for(int num : nums){
            if(num < bp) bp = num; 
            else{
                int currProfit = num - bp; 
                max = Math.max(currProfit, max); 
            }
        }

        return max; 
    }
}
