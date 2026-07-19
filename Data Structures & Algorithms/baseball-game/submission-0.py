class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == '+':
                sum_prev = record[-1] + record[-2]
                record.append(sum_prev)
            elif op == 'D':
                double_val = record[-1] * 2
                record.append(double_val)
            elif op == 'C':
                record.pop()
            else:
                score = int(op)
                record.append(score)

        return sum(record)