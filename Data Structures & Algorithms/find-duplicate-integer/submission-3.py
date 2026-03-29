class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        temp= [0] * len(nums)

        for i in nums:
            if temp[i-1] != 0:
                return i
            temp[i-1]= i