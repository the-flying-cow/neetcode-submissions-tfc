class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s= s.strip().lower()
        lst_s= s.split()

        s= "".join(lst_s)

        p, q= 0, len(s) - 1
        
        while p < q:
            if s[p].isalnum() == False:
                p+=1
                continue
            if s[q].isalnum() == False:
                q-=1
                continue

            if s[p] == s[q]:
                p+=1
                q-=1
            else:
                return False

        return True
            