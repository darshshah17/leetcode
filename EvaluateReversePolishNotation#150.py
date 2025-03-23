class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []

        for char in tokens:
            if char in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if char == "+":
                    stack.append(operand1 + operand2)
                elif char == "-":
                    stack.append(operand1 - operand2)
                elif char == "*":
                    stack.append(operand1 * operand2)
                else:
                    # necessary to do this because we want to truncate towards 0 
                    # but if we did //, it wouldn't work for negative #'s:
                    # e.g
                    # -5 // 130 = -1 not 0, which we don't want.
                    stack.append(int(operand1 / operand2))
            else:
                stack.append(int(char))

        return stack[0]


        