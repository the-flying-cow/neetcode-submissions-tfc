class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk= []
        for i in operations:
            if i == "+":
                x= stk[-1]
                y= stk[-2]
                stk.append(x+y)
            elif i == "D":
                x= stk[-1]
                stk.append(2*x)
            elif i == "C":
                stk.pop()
            else:
                stk.append(int(i))
        return sum(stk)
                