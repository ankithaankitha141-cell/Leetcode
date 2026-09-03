class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        has_odd = any(x % 2 != 0 for x in nums1)
        
        # If there are no odd numbers, all elements are already even.
        if not has_odd:
            return True
        
        # If the minimum element is odd, every even element is larger than min_val.
        # We can subtract min_val from any even number to make it odd (Even - Odd = Odd).
        if min_val % 2 != 0:
            return True
        
        # If min_val is even and there is at least one odd number:
        # - Making all odd is impossible (min_val cannot be reduced by a smaller odd number).
        # - Making all even is impossible (the smallest odd number cannot be reduced by a smaller odd number).
        return False
