class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # min_len[i] stores the minimum length of a valid subarray ending at or before index i
        min_len = [float('inf')] * n
        
        ans = float('inf')
        left = 0
        current_sum = 0
        best_till_now = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window if current_sum exceeds target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
                
            if current_sum == target:
                length = right - left + 1
                
                # Check if a non-overlapping valid subarray exists before 'left'
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, length + min_len[left - 1])
                
                best_till_now = min(best_till_now, length)
            
            # Record the shortest valid subarray found up to current index 'right'
            min_len[right] = best_till_now
            
        return ans if ans != float('inf') else -1