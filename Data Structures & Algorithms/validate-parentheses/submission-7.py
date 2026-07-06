class Solution:
    def isValid(self, s: str) -> bool:
        # since ordering matters, we have to use a stack
        parens = []
        for p in s:
            if p == ")":
                if not parens or parens.pop() != "(":
                    return False
            elif p == "}":
                if not parens or parens.pop() != "{":
                    return False
            elif p == "]":
                if not parens or parens.pop() != "[":
                    return False
            else:
                parens.append(p)
        return not parens
