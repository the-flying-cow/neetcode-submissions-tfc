class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        p, q= 0, len(numbers)-1
        sum= 0
        
        while p!=q:
            sum= numbers[p] + numbers[q]
            if sum==target:
                return [p+1, q+1]
            if sum > target:
                q-=1
            else:
                p+=1
            

        return []
