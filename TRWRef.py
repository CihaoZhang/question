# This problem is inspired from Leetcode's Trapping Rain Water -> #42

class Solution:
    def trap(self, height: List[int]) -> int:
        # Set up both pointers
        left = 0
        right = len(height) - 1

        # Instantiate variables for the maximum height (-1 because we will take the MAX, hence if it's 1000, it will take the default value)
        maxLeft = -1
        maxRight = -1

        # Instantiate variable for incrementation
        water = 0

        # we "Transverse" from left to right to check for the conditions
        while left < right:
            # Updates the maximums
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])

            # If left is smaller than right, it must mean that there is a puddle in between the wheel. We calculate possible puddles.
            if maxLeft < maxRight:
                water += maxLeft - height[left]
                left += 1
            else:
                water += maxRight - height[right]
                right -= 1

        return water