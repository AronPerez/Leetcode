class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        """
        if newInterval startTime greater than i's endtime and endTime is less than i+1's startTime
        We can insert it between the 2 intervals [[i], [i+1]]
                                                 here ^,
        """
        # Insert strictly based on the pos based on startTime
        
        pos = bisect.bisect(intervals, newInterval)
        intervals.insert(pos, newInterval)
        
        # if newInterval startTime less than interval i's endTime, there is overlap
        # We would need to make sure newInterval endTime is before i+1's startTime
        
        res = []
        
        for interval in intervals:
            if not res or res[-1][1] < interval[0]: # endTime of interval i less than startTime of newInterval
                res.append(interval) # [[1,3]]
            else:
                res[-1][1] = max(res[-1][1], interval[1])
            
        return res