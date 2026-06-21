class Solution:
    def isValid(self, s: str) -> bool:
        if not s :
            return False
        if s[0]=="}" or s[0]=="]" or s[0]==")":
            return False    
        if len(s)% 2 == 1  :
            return False
        
        stack=[]

        for i in range(0,len(s)):

            if s[i]=="{" or s[i]=="[" or s[i]=="(":
                stack.append(s[i])
            if s[i]=="}" or s[i]=="]" or s[i]==")"  :
                if len(stack) == 0:
                    return False

                top_item=stack.pop()
                
                if s[i]=="}" and top_item !="{":
                    return False
                if s[i]=="]" and top_item !="[":
                    return False
                if s[i]==")" and top_item !="(":
                    return False

        if len(stack) != 0 :
            return False
        return True