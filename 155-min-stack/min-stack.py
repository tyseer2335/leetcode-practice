class MinStack:  

    def __init__(self): 
        # Keep track of min so far seen so far 
        # Ie for the subarray thats i elements long (0 <= i <= self.stack) 
        # the ith element in self.min_so_far is the ith min so far 
        # So we can pop from both arrays to "backtrack" back to prevous min_so_far and  
        # last used stack value
        self.min_so_far = []
        self.stack = []

    def push(self, val: int) -> None:  
        # If stack is empty than its our min_so_far
        if len(self.stack) < 1: 
            self.min_so_far.append(val) 
        else:  
            # If we have multiple elements, add the min of our most recent 
            # element or val, this is the min so far, since if val is bigger 
            # we use our prevous min (which is indeed the prevous min)
            self.min_so_far.append(min(val, self.min_so_far[-1]))  

        # After updating min we append the value to the stack
        self.stack.append(val)

    def pop(self) -> None:   
        # Pop from both stacks to "backtrack" to a prevous state
        self.stack.pop()  
        self.min_so_far.pop()
        
    def top(self) -> int: 
        # Return the top element
        return self.stack[-1]
        
    def getMin(self) -> int:  
        # Most recent min is top of stack
        return self.min_so_far[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin() 

# Time Taken: 32:22 
# Time Complexity: O(1) 
# Space Complexity: O(n)

# NOTE We used a 'backtracking' strategy where we stored the state of prevous min so far values 
# in the future try thinking of using this method, needed a hint to get it