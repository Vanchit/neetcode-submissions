import math

class Solution:
    def minEatingSpeed(self, piles, h):
        min_speed = 1

        # Find maximum pile size
        max_speed = max(piles)

        # Binary Search
        while min_speed < max_speed:
            mid = min_speed + (max_speed - min_speed) // 2

            if self.canEatInTime(piles, h, mid):
                max_speed = mid
            else:
                min_speed = mid + 1

        return min_speed


    def canEatInTime(self, piles, h, speed):
        hours = 0

        for pile in piles:
            hours += math.ceil(pile / speed)

        return hours <= h