class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for p in numbers:
            q=  target-p
            if q in numbers and (numbers.index(p) < numbers.index(q)):
                return [numbers.index(p)+1, numbers.index(q)+1]
            