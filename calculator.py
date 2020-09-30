from collections import namedtuple

Operation = namedtuple('Operation', 'num1 num2 op')


class Calculator:

    def __init__(self):
        self.operations = {}

    def add(self, num1, num2):
        op = Operation(num1, num2, '+')
        return self.operations.setdefault(
            op, num1 + num2)

    def subtract(self, num1, num2):
        op = Operation(num1, num2, '-')
        return self.operations.setdefault(
            op, num1 - num2)

    def multiply(self, num1, num2):
        op = Operation(num1, num2, '*')
        return self.operations.setdefault(
            op, num1 * num2)

    def divide(self, num1, num2):
        op = Operation(num1, num2, '/')
        return self.operations.setdefault(
            op, num1 / num2)

    def print_operations(self):
        print('\n'.join(
            f"{op.num1} {op.op} {op.num2} = {int(ret)}"
            for op, ret in self.operations.items()
        ))
