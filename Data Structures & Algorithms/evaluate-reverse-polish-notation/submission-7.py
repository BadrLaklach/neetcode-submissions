class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for token in tokens:
            if token in ["+","-","/","*"]:
                a=stack.pop() #right element
                b=stack.pop() #left element
                if token == "+":
                    stack.append(b+a)
                if token == "-":
                    stack.append(b-a)
                if token == "*":
                    stack.append(b*a)
                if token == "/":
                    stack.append(int(b/a))



            else:
                stack.append(int(token))
        

        return stack[0]