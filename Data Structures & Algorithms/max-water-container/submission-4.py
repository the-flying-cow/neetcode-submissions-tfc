
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res= 0

        for i in range(0, len(heights)):

            for j in range(i+1, len(heights)):

                length= min(heights[i], heights[j])
                width= j - i
                area= length * width
                res= max(res, area)

        return res

                