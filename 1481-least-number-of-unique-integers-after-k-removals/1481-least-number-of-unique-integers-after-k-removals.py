class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        valueFreq = Counter(arr)
        
        # Min heap
        freqs = list(valueFreq.values())
        heapq.heapify(freqs)
        
        elementsRemoved = 0
        
        while freqs:
            # Remove least freq elements
            elementsRemoved += heapq.heappop(freqs)
            
            # If num of elements removed greater than k, we can return
            if elementsRemoved > k:
                # Add 1 to remaining element
                return len(freqs) + 1
            
        return 0
                