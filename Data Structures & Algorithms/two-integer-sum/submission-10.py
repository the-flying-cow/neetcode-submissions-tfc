class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res= []
        hash= {}
        for i, first in enumerate(nums):
            second= target-first
            if second in hash:
                res.append(hash[second])
                res.append(i)
            else:
                hash[first]= i
        return res