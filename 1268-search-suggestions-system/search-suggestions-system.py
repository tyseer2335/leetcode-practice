class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        # Our final resul 
        res = []  

        # Sort products in alphebetical order since we need to find the first 3 matches in that order
        products.sort()

        # Start the string at the first character and keep appending a character each time
        s = ""

        # Loop through the remaining characters
        for i in range(0, len(searchWord)): 

       
            temp = [] 

            # Increase our word s by one more character
            s += searchWord[i] 

            # For each word in products we need to match the first i characters to the first i of the word in repo
            for word in products:   
                    

                # Ensure both are in lowercase, since we are comparing non case sensitive
                s = s.lower()
                W = word[:i + 1].lower() # First i characters of word in repo

                # If the first i characters are the same
                if s == W: 
                    # Convert it to lowercase
                    out = word.lower() 

                    # Add it to the inner array (temp)
                    temp.append(out)  

                    # If adding that word makde the inner array length 3, than we found our first 3 words, so stop looking
                    if len(temp) == 3: 
                        break 
                
            # Sort the inner array to be in alphebetical order
            temp.sort() 

            # Add the inner array to temp to build the solution at each iteration
            res.append(temp)

        # Return the final result
        return res 

# Time Complexity: O(nm), where n is the length of searchWord and m is the length of products
# Space Complexity: O(m)

######################################################################################################################## 
# Better solution using a Trie
########################################################################################################################
# TODO 



