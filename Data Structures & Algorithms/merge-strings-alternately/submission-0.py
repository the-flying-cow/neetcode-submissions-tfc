class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr1= list(word1)
        m= len(arr1)
        arr2= list(word2)
        n= len(arr2)
        res= []

        i= 0
        j= 0

        while (i < m) and (j < n):
            res.append(arr1[i])
            res.append(arr2[j])
            i+= 1
            j+= 1
        
        while i < m:
            res.append(arr1[i])
            i+= 1

        while j < n:
            res.append(arr2[j])
            j+= 1
        
        return "".join(res)
        
