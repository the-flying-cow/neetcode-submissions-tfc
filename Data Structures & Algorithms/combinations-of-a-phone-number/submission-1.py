class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res= []
        digits_char= {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backTrack(i, curStr): # i tells the index, curStr tells the current string we are building
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for ch in digits_char[digits[i]]:
                backTrack(i + 1, curStr + ch)

        if digits:
            backTrack(0, "")

        return res