class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        l, r = 0, len(heights) - 1

        while l < r: 
            # smaller one becomes the height
            height = min(heights[l], heights[r])

            # width 
            width = r - l

            curr_vol = height * width

            res = max(curr_vol, res)

            # update l and r
            if heights[l] < heights[r]: 
                l += 1
            else: 
                r -= 1

            
        return res
        