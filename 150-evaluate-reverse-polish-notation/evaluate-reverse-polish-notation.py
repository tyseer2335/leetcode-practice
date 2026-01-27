import math as m

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:  

        # Add 2 elements to the stack 
        # When we see an operation pop 2 elements preform that operation, than add result back to stack 
        # Keep going until we processed all tokens, solution should be last element in stack 

        # Our valid operations and stack to keep track of most recent 2 numbers
        operations = {"*", "/", "+", "-"} 
        stack = []

        # Go through all tokens
        for token in tokens:     
            # Not operation => digit
            if token not in operations:  
                # Add the digit to stack and process next token
                stack.append(token) 
            else:  
                # Pop the first 2 elements 
                # We know we wont have an empty stack since  
                # that would be invalid RPN
                first = stack.pop() 
                second = stack.pop()   

                # Porcess each operation
                if token == "/":   
                    # NOTE 'truncate towards zero != floor lol this wasted time"
                    res = int(second) / int(first)    
                    # This is how we properly truncate towards zero 
                    if res > 0: 
                        res = m.floor(res)  
                    else:  
                        res = m.ceil(res)
                # Perform the operations, we need to convert to int 
                elif token == "*":  
                    res = int(first) * int(second) 
                elif token == "+":  
                    res = int(first) + int(second) 
                else:  
                    res = int(second) - int(first) 
                # Append back as a string  
                # (we dont need to as string,  
                # but since other digits are strings)
                stack.append(str(res))  
        
        # The last element (and only) is our solution, return as an int
        return int(stack[-1])

    # Time Taken: 25:03 
    # Time Complexity: O(n) 
    # Space Complexity: O(n)

