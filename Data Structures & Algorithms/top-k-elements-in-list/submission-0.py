class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter(nums)
        top_k= count.most_common(k)
        res= []
        for x in top_k:
            res.append(x[0])
        return res