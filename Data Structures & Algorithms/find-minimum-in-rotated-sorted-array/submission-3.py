class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low, high= 0, len(nums)-1
        min_num= nums[0]
        
        
        while low <= high:

            if nums[low] < nums[high]:
                min_num= min(min_num, nums[low])


            mid= low + (high-low)//2
            min_num= min(min_num, nums[mid])

            if nums[low] <= nums[mid]:
                low= mid+1
                
            else:
                high= mid-1
        
        return min_num