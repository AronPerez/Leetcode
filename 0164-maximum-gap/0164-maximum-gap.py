class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
    
        if n < 2:  # If the array contains less than two elements
            return 0  # Return 0

        min_val, max_val = min(nums), max(nums)  # Find the minimum and maximum values in the array

        if min_val == max_val:  # If all elements in the array are the same
            return 0  # Return 0

        # Calculate the size of each bucket
        bucket_size = max(1, (max_val - min_val) // (n - 1))

        # Calculate the number of buckets needed
        num_buckets = (max_val - min_val) // bucket_size + 1

        # Create buckets to store the minimum and maximum values in each bucket
        buckets = [[float('inf'), float('-inf')] for _ in range(num_buckets)]

        # Distribute the elements into the buckets
        for num in nums:
            index = (num - min_val) // bucket_size  # Calculate the bucket index for the current element
            buckets[index][0] = min(buckets[index][0], num)  # Update the minimum value in the bucket
            buckets[index][1] = max(buckets[index][1], num)  # Update the maximum value in the bucket

        # Find the maximum gap between adjacent buckets
        max_gap = 0  # Initialize the maximum gap to 0
        prev_max = min_val  # Initialize the previous maximum value to the minimum value in the array

        for bucket in buckets:
            if bucket[0] == float('inf'):  # If the bucket is empty
                continue  # Skip to the next bucket
            max_gap = max(max_gap, bucket[0] - prev_max)  # Update the maximum gap if necessary
            prev_max = bucket[1]  # Update the previous maximum value to the maximum value in the current bucket

        return max_gap  # Return the maximum gap
        