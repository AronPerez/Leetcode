class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)  # Get the number of jobs
    
        # Create a list of jobs with their start time, end time, and profit
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        dp = [0] * (n + 1)  # Create a DP array to store the maximum profit up to each job

        for i in range(1, n + 1):  # Iterate through each job
            current_profit = jobs[i - 1][2]  # Get the profit of the current job

            # Find the index of the previous non-overlapping job using binary search
            prev_job_index = bisect.bisect_right(jobs, jobs[i - 1][0], key=lambda x: x[1]) - 1

            # Calculate the maximum profit by considering the current job's profit
            # and the maximum profit from the previous non-overlapping jobs
            if prev_job_index != -1:
                dp[i] = max(current_profit + dp[prev_job_index + 1], dp[i - 1])
            else:
                dp[i] = max(current_profit, dp[i - 1])

        return dp[n]  # Return the maximum profit