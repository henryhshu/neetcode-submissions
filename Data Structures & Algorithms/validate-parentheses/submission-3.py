class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeParens = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in closeParens:
                if stack and closeParens[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0