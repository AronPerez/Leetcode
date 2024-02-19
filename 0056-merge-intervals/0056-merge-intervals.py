class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            Original approach (INCORRECT)
            
            # We want the start time value to be what we determine is overlapping
            
            # We store the start time i[0] IFF startTime == -1
            # Check if i+1[0] <= i[1], if it is, we have overlapping interval and don't store endtime yet
            # If the start time of the interval i+1 is <= the end endtime of i, set i[0] -> i+n[1]

            # We continue to the next interval @ i+1, do our little startTime check
            # We check if i+2[0] <= i[1]
                # If it isnt, we assign endtime and have an interval
                
            # Create interval only when startTime and EndTime arent -1
                # append to result
                # Set startTime and endTime to -1
        """
        # We want the start time value to be what we determine is overlapping
        intervals.sort(key= lambda x: x[0]) # [[1, 3], [2, 6], [8, 10], [15, 18]]
        # We have a start time
        
        res = []
        for interval in intervals: # 1, 2
            if not res or res[-1][1] < interval[0]: # if we have no res and or last value on res's end time is less than i intervals start time
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1]) # If we find a greater endtime for the last value in res, swap it
                                
        
        # return res    
        return res
        