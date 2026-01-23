class Solution:
    def isPalindrome(self, s: str) -> bool:   
        # All digits
        digits = {str(x) for x in range(0,10)}
         
        # Remove non alphanumeric characters 
        # Ensure to keep digits, since isalpha() filters them out 
        # Also make sure its in lowercase
        clean = "" 
        for i in s:  
            if i.isalpha(): 
                clean += i.lower() 
            elif i in digits: 
                clean += i

        # Reverse the string 
        rev = "" 
        for k in range(len(clean) - 1, -1, -1): 
                rev += clean[k]

        # Compare if they are the same
        return clean == rev
        
# Time Taken 7:21 
# Time Complexity O(n) 
# Space Complexity O(n) 
# NOTE: Please make sure you read the question and understand definition of alphanumeric in this question