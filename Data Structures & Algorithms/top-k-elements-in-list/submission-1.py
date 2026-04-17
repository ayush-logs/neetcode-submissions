class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums).most_common(k)
        res  = []
        for num in counter: 
            res.append(num[0])

        return res

        
        