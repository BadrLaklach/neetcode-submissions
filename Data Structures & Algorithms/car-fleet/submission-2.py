class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        
        result=0
        n=len(position)

        for i in range(0,n):
            stack.append([position[i],speed[i]])
    
        stack.sort()
        top=stack.pop()
        while stack: 
            HeadSteps=(target-top[0])/top[1]
            if HeadSteps >= ((target-stack[-1][0])/stack[-1][1]):
                stack.pop()
                continue
            else:
                top = stack.pop()
                result = result +1
        return result +1
