class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ")":
                if not (stack and stack.pop() == "("):
                    return False
            elif c == "}":
                if not (stack and stack.pop() == "{"):
                    return False
            elif c == "]":
                if not (stack and stack.pop() == "["):
                    return False
            else:
                stack.append(c)
        print(stack)
        return not stack
                