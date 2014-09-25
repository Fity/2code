class Solution:

    def __init__(self):
        self.operations = {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, '/': lambda x, y: x/y}

    def evalEPR(self, var1, var2, op):
        return int(self.operations.get(op)(var1, var2))

    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            elif token in self.operations:
                var2 = stack.pop()
                var1 = stack.pop()
                stack.append(self.evalEPR(float(var1), var2, token))
        if len(stack) == 1:
            return stack.pop()
        else:
            return 'Wrong Expression'
