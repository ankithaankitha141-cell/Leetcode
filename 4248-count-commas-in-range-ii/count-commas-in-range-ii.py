class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        threshold = 1000  # 10^3 (first threshold where numbers get 1 comma)
        
        while n >= threshold:
            total_commas += n - threshold + 1
            threshold *= 1000  # Move to the next threshold (10^6, 10^9, etc.)
            
        return total_commas


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    
    # Test Example 1
    print(sol.countCommas(1002))  # Output: 3
    
    # Test Example 2
    print(sol.countCommas(998))   # Output: 0
    
    # Large constraint check (10^15)
    print(sol.countCommas(10**15)) # Output: 2997000000000003