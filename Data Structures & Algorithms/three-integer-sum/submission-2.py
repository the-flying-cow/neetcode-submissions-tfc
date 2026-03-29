class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        count= collections.Counter(nums)
        res= []

        for i in range(len(nums)):
            count[nums[i]] -= 1

            if i and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1

                if j - 1 > i and nums[j] == nums[j-1]:
                    continue

                third_val= -(nums[i] + nums[j])
                if count[third_val] >= 1:
                    res.append([nums[i], nums[j], third_val])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1

        return res

