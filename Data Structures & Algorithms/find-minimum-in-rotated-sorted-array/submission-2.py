class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h= 0, len(nums)-1
        m= -1
        res= nums[0]
        while l <= h:
            if nums[l] < nums[h]:
                res= min(res, nums[l])
                break
            m= l + (h-l)//2
            res= min(res, nums[m])

            if nums[l] <= nums[m]:
                l= m + 1
            else:
                h= m - 1

        return res