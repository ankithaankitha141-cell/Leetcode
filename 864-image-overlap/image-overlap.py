from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Collect coordinates of all 1s
        list1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        list2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count translation vectors
        count = Counter()
        for r1, c1 in list1:
            for r2, c2 in list2:
                count[(r2 - r1, c2 - c1)] += 1
                
        # Return maximum overlapping 1s
        return max(count.values()) if count else 0