class Solution:
    def reverse(self, x: int) -> int: 

        # The min and max integer ranges defined in the problem
        MIN, MAX = -2**31, 2**31 - 1

        # Flag to determine if its negative (Since we dont reverse the negative sign)
        is_negative = False 

        # Negative check, we will turn it positive for now and flag this to handle later
        if x < 0: 
            is_negative = True  
            x = -x

        # Convert it into a string to reverse
        num = str(x) 
        
        # Edgecase with all zeros
        if x == 0: 
            return 0 

        # We will define a pointer at the end to get rid of the trailing zeros 
        # This introduces the Edgecase handled prevously
        p = len(num) - 1  
        
        # Keep track of p where the trailing zeros end (if any)
        while num[p] == "0": 
            p -= 1 

        # Chop off the trailing zeros
        num = num[:p + 1]   

        # Reverse the number
        rev = num[::-1]

        # If it was negative we need to turn it back into a positive 
        # This keeps the negative sign while reverseing the number
        if is_negative: 
            num = str(-int(num))
            rev = str(-int(rev))

        # If the reversed version does not fits in the defined range, return 0
        if not(MIN <= int(rev) <= MAX): 
            return 0  
        
        return int(rev)
        

# Time Taken: 17:31 
# Time Complexity: O(n),  
    # Where n = log_{10}(|n|), since as the digits of n increase lograthmically as n increases  
    # Here is why: https://i.ibb.co/F42yT6zX/666666.png
# Space Complexity O(n)

# There is a clever 'math' trick to solving this problem thats a bit better 
# https://youtu.be/HAgLH58IgJQ