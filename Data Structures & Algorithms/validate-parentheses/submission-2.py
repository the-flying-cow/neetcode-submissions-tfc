class Solution:
    def isValid(self, s: str) -> bool:
        if s=="":
            return True

        stack= []
        left_brackets= ['(', '{', '[']
        right_brackets= [')', '}', ']']
        
        for ch in s:
            if ch in left_brackets:
                stack.append(ch)
            elif ch in right_brackets:
                if stack and ((ch==')' and stack[-1]=='(') or (ch=='}' and stack[-1]=='{') or (ch==']' and stack[-1]=='[')):
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False