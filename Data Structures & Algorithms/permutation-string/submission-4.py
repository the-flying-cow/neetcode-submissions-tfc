from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        size= len(s1)
        count= Counter(s1)

        p= 0
        q= size-1

        while q < len(s2):
            temp_dict= count.copy()
            sum= 0
            
            window_dict= Counter(s2[p:q+1])
            if window_dict == temp_dict:
                return True

            p+= 1
            q+= 1
        
        return False
            