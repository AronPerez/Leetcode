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
        
        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                
        res.append(newInterval)
        
        return res