class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_k= float('inf')
        low, high= 1, max(piles)

        while low <= high:
            total_hrs= 0
            mid= low + (high-low)//2

            for i in piles:
                total_hrs+= math.ceil(i/mid)
            if total_hrs <= h:
                min_k=  min(min_k, mid)
                high= mid-1
            
            else:
                low= mid+1

        return min_k           

