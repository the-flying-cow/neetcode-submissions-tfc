class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res= [[]]
        nums.sort()

        def dfs(i, sub):

            if sub not in res:
                res.append(sub.copy())
                
            if i >= len(nums):
                return

            sub.append(nums[i])
            dfs(i+1, sub)

            sub.pop()
            dfs(i+1, sub)

        dfs(0, [])
        return res