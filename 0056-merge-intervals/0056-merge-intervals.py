class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Initialize an empty list to store the merged intervals.
        merged_intervals = []

        # Sort the intervals based on their start times.
        intervals.sort(key=lambda x: x[0])

        # Iterate over the sorted intervals.
        for interval in intervals:
            # If the merged_intervals list is empty or the interval's start time is greater than the end time of the last
            # interval in the merged_intervals list, then add the interval to the merged_intervals list.
            if not merged_intervals or interval[0] > merged_intervals[-1][1]:
                merged_intervals.append(interval)
            # Otherwise, merge the current interval with the last interval in the merged_intervals list.
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        # Return the merged intervals.
        return merged_intervals

