class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        
##########################################################################################################
# Original Approach
##########################################################################################################
        # res = [] # Result Array
        # seen = [] # Seen Hashmaps Array 

        # for word in strs:  
        #     # Built hashmap to tell anagrams for each word
        #     h_map = {}   
        #     for char in word: 
        #         if char not in h_map: 
        #             h_map[char] = 0 
        #         h_map[char] += 1  

        #     # If hashmap is not in seen, so we havent seen it before
        #     if h_map not in seen:
        #         res.append([word]) # Its a new anagram 
        #         seen.append(h_map) # See it
        #     else:  
        #         # If we have seen this pattern before, find the matching pattern 
        #         # in seen and add the word to the corresponding group in res
        #         for i in range(len(res)): 
        #             if seen[i] == h_map: 
        #                 res[i].append(word)

        # return res 

# Time taken 23:12
# Time Complexity O(n^2*k)
# Space Complexity O(n*k) 
# Where n is number of words in the input list and k is maximum length of a word in the list 

# NOTE: That this solution is not optimal, we can create a unique array for each word by making a 
# 26 letter array of 0s and incrementing it for each word seen, than using a hashmap to collect 
# anagrams and than finally loop through this hashmap with our groups 

##########################################################################################################
# Optimized
########################################################################################################## 

        # Store results as encodings as keys and values as the array of same anagrams 
        res = {} 

        # Set of seen encodings
        seen = set()
        
        # Aplabet mappings
        alpha = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9,
            "k": 10,
            "l": 11,
            "m": 12,
            "n": 13,
            "o": 14,
            "p": 15,
            "q": 16,
            "r": 17,
            "s": 18,
            "t": 19,
            "u": 20,
            "v": 21,
            "w": 22,
            "x": 23,
            "y": 24,
            "z": 25
        }

        # Loop through each world
        for word in strs: 
            # Make a template for the encoding
            encoding = [0] * 26 

            for char in word: 
                # For each char at the ith place in the alphebet 
                # Add one to that ith place in the encoding array
                encoding[alpha[char]] += 1 

            # 'Seal' the encoding since lists are not hashable
            encoding = tuple(encoding)

            # If we havent seen this encoding than see it, and add to result
            if encoding not in seen: 
                seen.add(encoding) 
                res[encoding] = [word] 
            else:  
                # Otherwuse find it and append word to it
                res[encoding].append(word)

        # Loop through all values and return it as an array
        return [x for x in res.values()] 

# Time Complexity O(n * k)
# Space Complexity O(n * k)
# Where n is number of words in the input list and k is maximum length of a word in the list 