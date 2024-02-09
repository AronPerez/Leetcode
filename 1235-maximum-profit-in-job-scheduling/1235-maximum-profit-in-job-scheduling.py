class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit)) # Sort ascending by start time
        n = len(jobs)
        
        # startA >= endB job A starts before job B ends
        # startB >= endA job B starts after job A ends
        
        # Combinatorics 2^n possible jobs to schedule where n is number of jobs
        
        # Schedule jobs at index i which end at end[i], then all jobs that have start time before then are discarded
        # The next job to schedule should have start[i] >= end[i] (must start at or after end)
        
        # Conflicting schedules + max profit by scheduling non-conflicting schedules lean towards DP
        
        
        # Top down approach starts from time zero/earliest start time
        # Since the jobs are sorted by ascending start time, we can use binary search
        # In our binary serch our target is the endTime
        
        """ Binary search 
        l, r = 0, len(nums) -1

        while l <= r:
            mid = l + ((r - l) // 2)

            if nums[mid] > target: # Number is bigger
                r = mid - 1
            elif nums[mid] < target: # Number is smaller
                l = mid + 1
            else:
                return mid

        return -1
        """
        
        def binarySearchHelper(endTime: int) -> int:
            l, r = 0, n - 1
            while l <= r:
                m = l + ((r-l)//2)
                start, end, profit = jobs[m] # Find at the middle point
                if start < endTime: # If our start is less than the endtime if what we are looking at
                    l = m + 1 # Move the left up
                else: # If the start is before endTime, we can move right down
                    r = m - 1
            return l
                    
        
        
        @cache
        def dfs(i: int) -> int:
            # When we run out of intervals
            if i == n:
                return 0
    
            # j = bisect.bisect(jobs, (jobs[i][1], -1, -1)) # Binary search, looking for the end time
            j = binarySearchHelper(jobs[i][1])
            
        
            return max(dfs(i + 1), jobs[i][2] + dfs(j))
        
        return dfs(0) # Start from 0 and go until we have max ans