class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res= float('inf')
        currentSum= 0
        L= 0        

        for R in range(len(nums)):

            currentSum += nums[R]

            while currentSum >= target:
                res= min(res, R-L+1)
                currentSum -= nums[L]
                L+= 1

        return res if res != float('inf') else 0