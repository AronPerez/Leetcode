class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        """
        if newInterval startTime greater than i's endtime and endTime is less than i+1's startTime
        We can insert it between the 2 intervals [[i], [i+1]]
                                                 here ^,
        """
        # Insert strictly based on the pos based on startTime
        # if newInterval startTime less than interval i's endTime, there is overlap
        # We would need to make sure newInterval endTime is before i+1's startTime
        
        result = []
        i = 0

        # Add intervals that come before the new interval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals 
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), 
                            max(intervals[i][1], newInterval[1])]
            i += 1
        result.append(newInterval)  

        # Add any remaining intervals
        result += intervals[i:]

        return result