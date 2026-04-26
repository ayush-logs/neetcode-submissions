class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        res = [0] * len(arr)
        mx = -1

        for i in range(n, -1, -1): 
            res[i]  = mx
            mx  = max(arr[i], mx)

        return res

        