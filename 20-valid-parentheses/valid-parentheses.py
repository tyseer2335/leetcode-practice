class Solution:
    def isValid(self, s: str) -> bool: 

        # Stack to store most recent bracket
        stack = [] 

        # Loop through each bracket
        for bracket in s:   
            # If its open bracket
            if bracket in {"(", "[", "{"}:  
                # Add it to the stack (most recently seen)
                stack.append(bracket) 
            else:  
                # If its a close bracket
                if not stack:  
                    # If our stack is empty ie something like this '((()'
                    return False 
                else:  
                    # Non empty, check if the right bracket closed our most recent bracket
                    prev = stack.pop() 
                    if (prev == "(" and bracket != ")") or (prev == "{" and bracket != "}") or (prev == "[" and bracket != "]"):  
                        # If not than we can return false, this is not valid parenthesis
                        return False

        # If we have something like '()(' than our stack will not be empty (final check)
        return stack == []
                
# Time taken: 16:03 
# Time Complexity: O(n) 
# Space Complexity: O(n) 
# Where n is the number of characters in s