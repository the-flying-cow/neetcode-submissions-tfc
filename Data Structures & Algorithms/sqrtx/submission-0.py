class Solution:
    def mySqrt(self, x: int) -> int:
        res= 0
        l, h= 0, x

        while l <= h:

            m= (l + h)//2

            if m*m > x:
                h= m-1
            elif m*m < x:
                res= m
                l= m+1
            else:
                return m
        return res