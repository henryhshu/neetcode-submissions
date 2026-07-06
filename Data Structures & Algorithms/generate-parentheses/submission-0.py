class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # can add open anytime as long as less than N
        # can add closed if less than open count
        stack = []
        res = []
        def backtrack(openCount, closedCount):
            if openCount == closedCount == n:
                res.append("".join(stack))
            if openCount < n:
                stack.append("(")
                openCount += 1
                backtrack(openCount, closedCount)
                stack.pop()
                openCount -= 1
            if closedCount < openCount:
                stack.append(")")
                closedCount += 1
                backtrack(openCount, closedCount)
                stack.pop()
        backtrack(0, 0)
        return res