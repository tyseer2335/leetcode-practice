class Solution:

    def encode(self, strs: List[str]) -> str:  
        # Count the string and add a '#' marker at the end 
        # Decoded string example => length#string

        s = ""  
        for stringy in strs:   
            # Length + '#'
            s += str(len(stringy)) + "#"  
            # The contents of the string
            s += stringy

        # Return the decoded string
        return s
    

    def decode(self, s: str) -> List[str]:   
        # Loop through and read how long it is, 
        # Save the string depending on length and append 
        # Some crazy pointer magic here 

        res = [] # Result array
        
        p = 0 # Pointer to keep track of string
        
        # Loop through the word
        while p < len(s): 

            # 1) Count how long the word is
            count = "" 
            while s[p] != "#":  # While we dont see a # we keep counting
                count += s[p] 
                p += 1 

            word = "" # Constructed word

            # 2) Loop count times, since thats length of word
            for i in range(int(count)):  
                word += s[p + i + 1] # Add those letters to word

            # Jump the pointer to end of word, start of next word length
            p += int(count) + 1  

            # Append the word we just decoded
            res.append(word)

        # Return the array of decoded words
        return res

    # Example:
        # ["n7et","co#e","love","you"] 
        # =>  4#n7et4#co#e4#love3#you 

    # Time Taken: 20:31 
    # Time Complexity: O(n) 
    # Space Complexity O(n)  
    # Where n is the length of the string
