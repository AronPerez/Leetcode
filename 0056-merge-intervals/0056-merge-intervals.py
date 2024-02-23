class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals based on their starting points.
        intervals.sort(key=lambda x: x[0])

        # Initialize an empty result list.
        result = []

        # Iterate through the sorted intervals.
        for interval in intervals:
            # Check if the current interval overlaps with the previous interval.
            if result and interval[0] <= result[-1][1]:
                # Merge the two intervals.
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                # Add the interval to the result list.
                result.append(interval)

        # Return the result list.
        return result
