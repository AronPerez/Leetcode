class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit)) # Sort ascending by start time
        jobs.sort(key= lambda x: x[0])
        cache = {}
        
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
        
        def dfs(i):
            # When we run out of intervals
            if i == len(jobs):
                return 0
            if i in cache:
                return cache[i]
            
            # Dont include
            res = dfs(i + 1)
        
            # Include
    
            j = bisect.bisect(jobs, (jobs[i][1], -1, -1)) # Binary search, looking for the end time
            
            
            cache[i] = res = max(res, jobs[i][2] + dfs(j))
            return res
        
        return dfs(0) # Start from 0 and go until we have max ans