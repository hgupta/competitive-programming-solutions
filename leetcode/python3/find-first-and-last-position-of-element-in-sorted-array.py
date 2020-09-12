# question url: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisect(is_left):
            # variant of array bisection algorithm
            # where we keep on searching the value
            # either to left or right of current found index

            # parameter: is_left -> to look left or right
            # left -> minimum, right -> maximum

            lo, hi = 0, len(nums) - 1
            found = -1

            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if target > nums[mid]:
                    lo = mid + 1
                elif target < nums[mid]:
                    hi = mid - 1
                else:
                    found = mid
                    if is_left:
                        hi = mid - 1
                    else:
                        lo = mid + 1
            return found

        return [bisect(True), bisect(False)]
