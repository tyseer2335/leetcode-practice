class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # The idea for this question is to keep a monotonic stack to keep track 
        # of decreasing temp days and go back to those days once we find a warmer day
        
        # We keep 'fill in' res non sequentially so we define an array of 0s
        res = [0 for x in range(len(temperatures))]   

        # To keep track of decresing temps and their indexes
        stack = []  
        indexes = []

        # Pointer (but since we are looping once we could of used a for loop)
        p = 0 

        # While pointer is valid
        while p < len(temperatures):  
            
            # If our stack is empty than we need to add the pth value as temperature to our stack and look next
            if stack == []:
                stack.append(temperatures[p])  
                indexes.append(p)
                p += 1 
            
            # If our stack is non empty and pointer is valid and finally  
            # If top of stack is smaller than p 
            # This means p is a warmer day, for stack[-1] 

            # Proof 
            # For this is because stack[-1] is the last coldiest day and p is warmer thus we need to  
            # compute the days between stack[-1] and p, and add it in stack[-1]th  
            # position since p - i is a warmer temp  
            # We countine to pop elements and fill them in arrordingly
            while (stack != []) and p < len(temperatures) and (stack[-1] < temperatures[p]):  
                i = indexes.pop()
                stack.pop()   
                res[i] = p - i 

            # Now the next temp is too low, so we add it to the stack and run the algoritm above
            while (stack != []) and p < len(temperatures) and (stack[-1] >= temperatures[p]):     
                stack.append(temperatures[p])   
                indexes.append(p)
                p += 1 

        # The last elemets are 0 so we dont need to handle this case
        return res 

        # Time Taken: Could not solve without help :(  
        # Time Complexity O(n) 

        # Next step try doing it with a for loop