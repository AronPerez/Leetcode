class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
        Multiply odd by 2 = even
        Deviation is max - min
        
        What if we get the max (if even) and divide by 2
        
        Repeat process where possible on max
        
        When the max value is odd, we can only multiply which means we cannot go down further
        
        """
        # Sort the array in ascending order
        # nums.sort()

        # Create a heap to store the minimum deviation of the array so far
        # Max heap
        heap = []
        minValue = float('inf')
        # Iterate through the array and add each element to the heap
        for num in nums:
            if num % 2 == 0: # If even
                heap.append(-num)
            else: # Odd
                num *= 2 # Allows us to get even value
                heap.append(-num) 
                
            minValue = min(minValue, num)

        heapq.heapify(heap)
        # Initialize the minimum deviation to the difference between the maximum and minimum elements in the array
        minDeviation = float('inf')
        # While the heap is not empty
        while heap:
            # Pop the max element from the heap
            maxValue = -heapq.heappop(heap)
            # Update the minimum deviation if necessary
            minDeviation = min(minDeviation, maxValue - minValue)
            # If the minimum element is even, add it back to the heap after dividing it by 2
            if maxValue % 2 == 0:
                minValue = min(minValue, maxValue//2)
                heapq.heappush(heap, -maxValue//2) # Add it back to the queue 
            else: # is odd and we cannot get lower
                break

        # Return the minimum deviation
        return minDeviation


        
