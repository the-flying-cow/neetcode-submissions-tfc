class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area= 0
        size= len(heights)
        
        i= 0
        j= size-1

        while i <= j:
            width= abs(j-i)
            height= min(heights[i], heights[j])

            area= width*height
            max_area= max(area, max_area)
            if heights[i] < heights[j]:
                
                i+=1
            else:
                j-=1

        return max_area
