class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], workers: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort(key = lambda x: x[0]) # sort jobs by skill ascending
        workers.sort() # Ascending skill
        maxProfit = i = maxProfitJob = 0

        """
        
        [2,4,6,8,10]
        [10,20,30,40,50]
        [4,5,6,7]
        """
        # iterate through workers
        for worker in workers: # 4, 5, 6, 7
            
            # Each worker only does 1 job since we are assigning only the max of maxProfitJob
            # Since i is at 2 and we sort workers by skill, we pickup from where we left off
            while i < len(jobs) and worker >= jobs[i][0]: # Go through jobs and while their skills is enough, get the best paying job
                maxProfitJob = max(maxProfitJob, jobs[i][1])
                i += 1
            
            # When we are done, add the maxProfitJob to maxProfit
            # If there is no job this worker can work, it's just 0 + 0
            maxProfit += maxProfitJob # 20, 40, 70, 100
            
            
        return maxProfit