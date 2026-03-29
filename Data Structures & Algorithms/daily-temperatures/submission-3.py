class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res= [0] * len(temperatures)
        stack= []
        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                
                prev_temp, prev_i= stack.pop()
                diff= i - prev_i
                res[prev_i]= diff

            stack.append((temp, i))

        return res
