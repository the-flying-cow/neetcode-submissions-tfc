class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p, q= 0, len(heights) - 1

        max_area= 0

        while p!=q:

            width= q - p
            length= min(heights[p], heights[q])

            area= length * width
            max_area= max(area, max_area)

            if heights[p] < heights[q]:
                p+=1

            else:
                q-=1

        return max_area