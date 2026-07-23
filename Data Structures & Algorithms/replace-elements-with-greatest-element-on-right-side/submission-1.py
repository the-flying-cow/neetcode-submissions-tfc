class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size= len(arr)

        maxVal= -1
        rMax= -1

        for i in range(size - 1, -1, -1):
            maxVal= max(rMax, arr[i])
            arr[i]= rMax
            rMax= maxVal

        return arr