class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash= set(nums)

        for i in hash:
            if (target - i) in hash:

                first= i
                second= target - i

        res= []
        for i in range(len(nums)):
            if nums[i] == first or nums[i] == second:
                res.append(i)

        return res