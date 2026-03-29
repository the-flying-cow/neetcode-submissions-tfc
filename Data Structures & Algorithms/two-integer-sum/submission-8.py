class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):

            first= nums[i]
            second= target - first

            for j in range(i+1, len(nums)):

                if nums[j] == second:
                    return [i, j]

        