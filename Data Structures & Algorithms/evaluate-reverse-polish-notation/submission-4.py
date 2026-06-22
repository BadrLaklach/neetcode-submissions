class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "*", "-", "/"]:
                a = stack.pop()  # right operand
                b = stack.pop()  # left operand
                
                if token == "+":
                    stack.append(b + a)
                elif token == "*":
                    stack.append(b * a)
                elif token == "-":
                    stack.append(b - a)   
                elif token == "/":
                    stack.append(int(b / a)) 
            else:
                stack.append(int(token))
        
        return stack[0]