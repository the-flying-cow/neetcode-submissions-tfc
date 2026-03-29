class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= "".join(s.split()).lower().strip()
        new_s= ""
        for ch in s:
            if ch.isalnum():
                new_s= new_s + ch
        return (new_s == new_s[::-1])
            