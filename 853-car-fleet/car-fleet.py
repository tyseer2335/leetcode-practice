class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """ 

        # Stack will store cars that form distinct fleets.
        # Each entry represents the "lead" car of a fleet.
        stack = []

        # Pair each car's position with its speed
        data = [(position[x], speed[x]) for x in range(len(position))]

        # Sort cars by their starting position (ascending)
        data.sort()

        # Edge case: if there is only one car, it forms exactly one fleet
        if len(data) == 1: 
            return 1

        # Start with the car closest to the target (rightmost car)
        # This car will always form a fleet
        stack.append(data[-1])

        # Traverse cars from right to left (from closest to farthest)
        for i in range(len(position) - 2, -1, -1):   

            # Get the front (leading) car of the current fleet
            front_pos, front_speed = stack[-1][0], stack[-1][1]

            # Time taken by the front car to reach the target
            time_for_front_car = float((target - front_pos)) / float(front_speed)

            # Current car's position and speed
            back_pos, back_speed = data[i][0], data[i][1]

            # Time taken by the current car to reach the target
            time_for_back_car = float((target - back_pos)) / float(back_speed)

            # If the current car takes longer to reach the target,
            # it cannot catch up to the front fleet, so it forms a new fleet
            if time_for_back_car > time_for_front_car: 
                stack.append(data[i]) 
        
        # Number of fleets is equal to the number of entries in the stack
        return len(stack)

# Time Complexity: O(n log n) due to sorting
# Space Complexty: O(n)