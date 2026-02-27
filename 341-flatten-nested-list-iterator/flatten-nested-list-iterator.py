# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]): 

        # Remove the nesting and treat it like normal array   
        # This recursive function should return flattened nested list 

        def flatten(n):  
            # Since n can be of type [NestedInteger] or NestedInteger
            # We have 2 cases

            # If its list than we iterate through it and 
            if isinstance(n, list):  
                res = [] 
                for x in n:  
                    # For each list recurse down the list
                    res.extend(flatten(x)) 
                return res 
            else:  

                # Base Case if n holds only a single integer
                if n.isInteger(): 
                    # Return it as an integer
                    return [n.getInteger()] 
                else: 
                    # Recurse down the list
                    return flatten(n.getList()) 

        # Make our nestedList just a flat list, question becomes easy now
        self.nestedList = flatten(nestedList) 

        # Index for the iterator
        self.index = 0 

    
    def next(self) -> int: 
        val = self.nestedList[self.index] 
        self.index += 1 
        return val
        
    
    def hasNext(self) -> bool: 
        return self.index < len(self.nestedList)
         
# Time Taken: 31:39 
# Time Complexity: O(n) 
