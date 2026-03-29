class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_Set= set(nums)
        max_sequence= 0
        
        for num in nums_Set:
            if num-1 not in nums_Set:
                current_sequence= 1
                while (num + current_sequence) in nums_Set:
                    current_sequence+=1
                max_sequence= max(max_sequence, current_sequence)
            
        return max_sequence
