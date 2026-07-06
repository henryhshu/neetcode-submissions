class Solution:
    def decodeString(self, s: str) -> str:
        # input string is always valid
        # use a stack to act as a natural recursive unfurler
        stack = []
        for i in range(len(s)):
            # push until we need to start decoding
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    # prepend the previous char
                    substr = stack.pop() + substr
                # pop the open bracket
                stack.pop()

                # find the multiplier
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                # push the whole inner part onto the stack
                stack.append(int(k) * substr)
            
        return "".join(stack)
                

            
