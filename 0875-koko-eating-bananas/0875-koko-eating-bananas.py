class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # 1, 11
        ans = r # 11

        # binary search
        while l <= r:
            m = (l + r ) // 2 # 6/ 5+1=6/2 -> 3/ 4+5=9/2 -> 4
            hrs = 0 # 0

            # Calcc total hours to eat all nanaers in current pile at current speed
            for naners in piles:
                hrs += math.ceil(naners/m)  # 0.5 -> 1, 2, 4, 6/ 1, 3, 6, 10/1, 3, 5, 8

            # Update ans and determine if we need to explore lower or higher speeds
            if hrs <= h: # Explore lower speeds
                ans = min(ans, m) # 6/ 4

                r = m - 1 # 5, 3
            else: # Faster speeds
                l = m + 1 # 4

        return ans # 4
        