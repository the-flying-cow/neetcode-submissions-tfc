class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []
        operators= ['+', '-', '*', '/']
        for val in tokens:
            if val in operators:
                b= int(stack.pop())
                a= int(stack.pop())
                if val=="+":
                    stack.append(int(a+b))
                if val=="-":
                    stack.append(int(a-b))
                if val=="*":
                    stack.append(int(a*b))
                if val=="/":
                    stack.append(int(a/b))
            else:
                stack.append(int(val))

        return int(stack.pop())
