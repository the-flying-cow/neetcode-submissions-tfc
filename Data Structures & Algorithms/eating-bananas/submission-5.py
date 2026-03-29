class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right= 1, max(piles)

        val= right

        while left <= right:

            k= (left + right)//2

            total= 0
            for p in piles:
                total += math.ceil(p / k)

            if total <= h:
                val= min(val, k)
                right= k  - 1
            else:
                left= k + 1

        return val