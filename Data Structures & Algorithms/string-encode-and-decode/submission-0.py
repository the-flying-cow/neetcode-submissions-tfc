class Solution:

    def encode(self, strs: List[str]) -> str:
        coded_str= ""
        for i in strs:
            coded_str += str(len(i)) + "*" + i

        return coded_str

    def decode(self, s: str) -> List[str]:
        decoded_list= []
        i= 0

        while i < len(s):

            j= i
            while s[j]!="*":
                j+= 1
            
            str_length= int(s[i:j])
            decoded_list.append(s[j+1: j+ 1+ str_length])
            i= j + 1+ str_length
 
        return decoded_list