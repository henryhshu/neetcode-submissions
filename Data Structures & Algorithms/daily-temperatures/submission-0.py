class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use stack that stores temp and index
        result = [0] * len(temperatures)
        stack = [] # stores temp and index
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp = stack.pop()
                result[temp[1]] = i - temp[1]
            stack.append([temperatures[i], i])
        return result