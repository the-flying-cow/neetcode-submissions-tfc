class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size= len(nums)
        res= [0]*size
        left= [0]*size
        right= [0]*size
        left[0], right[size-1]= 1, 1

        for i in range(1, size):
            left[i]= left[i-1] * nums[i-1]
        for i in range(size-2, -1, -1):
            right[i]= right[i+1] * nums[i+1]
        for i in range(size):
            res[i]= left[i] * right[i]
        return res      