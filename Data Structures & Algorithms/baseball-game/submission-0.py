class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # all operations are valid
        # there are only three operations besides numbers: "+", "D", and "C"
        ops = []
        for i in range(len(operations)):
            if operations[i] == "+":
                ops.append(ops[-1] + ops[-2])
            elif operations[i] == "D":
                ops.append(2 * ops[-1])
            elif operations[i] == "C":
                ops.pop()
            else:
                ops.append(int(operations[i]))
        return sum(ops)
            

