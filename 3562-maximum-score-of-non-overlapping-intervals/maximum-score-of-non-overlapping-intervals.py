from bisect import bisect_left
from typing import List


class Solution:

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Store as (l, r, weight, original_index)
        arr = [
            (intervals[i][0], intervals[i][1], intervals[i][2], i)
            for i in range(n)
        ]

        # Sort intervals by end time (r), then start time (l), then original index
        arr.sort(key=lambda x: (x[1], x[0], x[3]))

        # Collect right boundaries for binary search
        rights = [x[1] for x in arr]

        # dp[k][i] = (max_weight, lexicographically_smallest_tuple_of_indices)
        # using up to k intervals from prefix arr[0...i-1]
        dp = [[(0, ())] * (n + 1) for _ in range(5)]

        for i in range(1, n + 1):
            l, r, w, idx = arr[i - 1]

            # Find largest j (1-based) such that arr[j-1].r < l
            j = bisect_left(rights, l)

            for k in range(1, 5):
                # Option 1: Skip interval arr[i-1]
                res_weight, res_path = dp[k][i - 1]

                # Option 2: Include interval arr[i-1]
                prev_weight, prev_path = dp[k - 1][j]
                take_weight = prev_weight + w

                # Maintain sorted original indices for lexicographical comparison
                take_path = tuple(sorted(prev_path + (idx,)))

                # Choose option with higher weight, or lexicographically smaller indices on tie
                if take_weight > res_weight:
                    dp[k][i] = (take_weight, take_path)
                elif take_weight == res_weight:
                    if not res_path or take_path < res_path:
                        dp[k][i] = (take_weight, take_path)
                    else:
                        dp[k][i] = (res_weight, res_path)
                else:
                    dp[k][i] = (res_weight, res_path)

        # Best result across choosing 1, 2, 3, or 4 intervals
        best_weight = 0
        best_path = ()

        for k in range(1, 5):
            w, path = dp[k][n]
            if w > best_weight:
                best_weight = w
                best_path = path
            elif w == best_weight and w > 0:
                if not best_path or path < best_path:
                    best_path = path

        return list(best_path)