class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 

        # Define 2 hashmaps that we will keep track of letters 
        # and corresponding counts
        h1 = {} 
        h2 = {} 

        # Loop through strings and count
        for i in s: 
            if i not in h1: 
                h1[i] = 1 
            else: 
                h1[i] += 1  

        # Same thing ....
        for k in t: 
            if k not in h2: 
                h2[k] = 1 
            else: 
                h2[k] += 1  

        # If they are the same than we must have an anagram else its not
        return h1 == h2
                
        # Time taken 4:31
        # Time Complexity O(n)
        # Space Complexity O(n) 
        # Where n is len(s) + len(t)