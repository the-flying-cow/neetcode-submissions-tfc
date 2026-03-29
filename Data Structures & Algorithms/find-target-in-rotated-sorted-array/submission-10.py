class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high= 0, len(nums)-1
        
        while low <= high:
            mid= low + (high-low)//2
            if target == nums[mid]:
                return mid
            
            if nums[low] <= nums[mid]: # left part sorted
                if target >= nums[low] and target < nums[mid]:
                    high= mid-1    
                else:
                    low= mid+1
            else: # right part sorted
                if target > nums[mid] and target <= nums[high]:
                    low= mid+1    
                else:
                    high= mid-1
            
        return -1