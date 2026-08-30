class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        # Find indices of min and max elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Determine smaller (i) and larger (j) indices
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)
        
        # Option 1: Both from front -> j + 1
        # Option 2: Both from back  -> n - i
        # Option 3: Both sides      -> (i + 1) + (n - j)
        return min(j + 1, n - i, (i + 1) + (n - j))