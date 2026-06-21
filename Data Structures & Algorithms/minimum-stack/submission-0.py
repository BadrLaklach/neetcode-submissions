class MinStack:
    def __init__(self):
        # Main stack stores all elements in LIFO order
        self.stack = []
        # Auxiliary stack stores the minimum value seen so far (strictly non-increasing)
        # This allows O(1) access to the current minimum
        self.minStack = []
    
    def push(self, val: int) -> None:
        # Always push to the main stack
        self.stack.append(val)
        
        # Push to minStack only if it's the new minimum (or first element)
        # We use <= so that duplicates of the minimum are also tracked
        # This ensures correct behavior when popping duplicate mins
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
    
    def pop(self) -> None:
        # Pop from main stack
        if self.stack:
            topElement = self.stack.pop()
            
            # If the element we just removed was the current minimum,
            # we also remove it from the minStack
            if self.minStack and topElement == self.minStack[-1]:
                self.minStack.pop()
    
    def top(self) -> int:
        # Return the top element without removing it
        # Safe because problem guarantees non-empty when called
        return self.stack[-1]
    
    def getMin(self) -> int:
        # Return current minimum in O(1)
        # Safe because problem guarantees non-empty when called
        return self.minStack[-1]