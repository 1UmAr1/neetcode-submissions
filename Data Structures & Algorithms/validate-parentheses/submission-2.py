class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_list = {
            ")": "(",
            "]": "[",
            "}": "{"
            }
        for c in s:
            if c in brackets_list:
                if stack and stack[-1] == brackets_list[c]:
                    stack.pop()
                
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False
            