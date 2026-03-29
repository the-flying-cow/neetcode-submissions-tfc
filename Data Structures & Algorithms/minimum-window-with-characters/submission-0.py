class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT= {}
        for ch in t:
            countT[ch]= 1 + countT.get(ch, 0)
        
        res= [-1, -1]
        resLen= float('infinity')

        for i in range(len(s)):
            countS= {}
            for j in range(i, len(s)):
                countS[s[j]]= 1 + countS.get(s[j], 0)

                flag= True

                for ch in countT:
                    if countT[ch] > countS.get(ch, 0):
                        flag= False
                        break

                if flag and (j -i + 1) < resLen:
                    resLen= j - i + 1
                    res= [i, j]

        l, r= res
        return s[l: r + 1] if resLen != float('infinity') else ""