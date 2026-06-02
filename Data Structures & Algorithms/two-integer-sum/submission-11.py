class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res= []
        hashMap= {}
        
        for idx, val in enumerate(nums): 

            if target - val in hashMap:
                res.append(hashMap[target-val])
                res.append(idx)
            else:
                hashMap[val]= idx

        return res