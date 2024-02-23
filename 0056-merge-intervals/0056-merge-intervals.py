class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort the intervals by their start time
        intervals.sort(key=lambda x: x[0])

        # Initialize the merged intervals list
        merged = []

        # Iterate over the intervals
        for interval in intervals:
            # If the current interval overlaps with the last interval in the merged list,
            # merge them
            if merged and interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            # Otherwise, add the current interval to the merged list
            else:
                merged.append(interval)

        return merged

