class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # possible operators: + - * /
        # division truncates, we should use //
        # 1 2 + => 3
        # 1 2 + 3 * => 9 [9]
        # is it possible to have three or more operands before hitting a operator?
        # are the operands always integers?
        # can we have negative operands?
        # can we have zero as operands?
        # is it possible to have two operands in a row?
        # what is the maximum length of the operands?
        # approach: we can use a stack to store the operands
        # when we reach an operator, we can pop the last two operands in the stack and operate on them
        # iterate through all of the tokens
        stack = []
        # iterate
        for token in tokens:
            # print(stack)
            if token == "+":
                stack.append(stack.pop() + stack.pop())
                continue
            if token == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
                continue
            if token == "*":
                stack.append(stack.pop() * stack.pop())
                continue
            if token == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
                continue
            stack.append(int(token))
        return stack[0]
