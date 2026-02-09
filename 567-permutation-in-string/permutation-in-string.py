class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:   

        # Edgecases 1:
        # One letter windows (just check the s2 for that one letter) 
        if len(s1) == 1: 
            if s1 in s2: 
                return True 
            else: 
                return False 

        # Edgecases 2:  
        # If s1 > s2 than its False *since the permutations we are looking for is longer that the string itself)
        if len(s1) > len(s2): 
            return False

        # Init sliding window 
        p1 = 0 
        p2 = len(s1) - 1  

        # Init the hashmap for window 
        window_hmap = {x:0 for x in  
            ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",  
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]}  

        for i in range(0, len(s1)):  # Populate the hashmap with contents
            window_hmap[s2[i]] += 1  

        # Init the hashmap for letter   
        letter_hmap = {x:0 for x in  
            ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",  
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]}   

        for i in range(0, len(s1)):  # Populate the hashmap with contents
            letter_hmap[s1[i]] += 1   


        # Check if they are a permutation 
        if letter_hmap == window_hmap: 
            return True

        # Slide the window across and update window_hmap check at the end of each slide   
        while p2 < len(s2) - 1:   

            window_hmap[s2[p1]] -= 1 # Since we shift window up this goes away 
            p1 += 1 
            p2 += 1 
            window_hmap[s2[p2]] += 1 # Add the new element we see  

            # Compare Hashmaps  
            if letter_hmap == window_hmap: 
                return True   

        # If we reach the end than no permutation has been found
        return False

# Time Taken: 35:29 

        
            





        