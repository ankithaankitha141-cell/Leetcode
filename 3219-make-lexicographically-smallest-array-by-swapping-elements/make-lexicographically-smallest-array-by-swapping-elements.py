class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Pair each value with its original index and sort by value
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
        
        n = len(nums)
        ans = [0] * n
        
        # Group elements into connected components
        i = 0
        while i < n:
            j = i + 1
            # Find the contiguous range of elements where difference between adjacent elements <= limit
            while j < n and sorted_nums[j][0] - sorted_nums[j - 1][0] <= limit:
                j += 1
            
            # Extract indices in this component and sort them
            indices = sorted(sorted_nums[k][1] for k in range(i, j))
            
            # Assign sorted values to sorted indices
            for k in range(i, j):
                val = sorted_nums[k][0]
                idx = indices[k - i]
                ans[idx] = val
            
            i = j
            
        return ans