class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size= len(arr)

        for i in range(size-1):
            
            maxVal= -1
            for j in range(i+1, size):
                if arr[j] > maxVal:
                    maxVal= arr[j]
            
            arr[i]= maxVal

        arr[size-1]= -1
        return arr