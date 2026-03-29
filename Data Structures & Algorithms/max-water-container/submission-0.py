class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area= 0
        size= len(heights)
        for i in range(size):
            for j in range(i+1, size):
                height= min(heights[i], heights[j])
                width= abs(j-i)
                area= height * width
                max_area= max(max_area, area)

        return max_area