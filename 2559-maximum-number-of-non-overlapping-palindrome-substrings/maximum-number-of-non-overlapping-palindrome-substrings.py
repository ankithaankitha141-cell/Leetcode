class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1  # End index of the last selected palindrome

        for i in range(2 * n - 1):
            # Center can be a character (i // 2) or between characters
            l = i // 2
            r = l + (i % 2)

            while l >= 0 and r < n and s[l] == s[r]:
                # Only consider palindromes after the last chosen one
                if l <= last_end:
                    break

                length = r - l + 1
                if length >= k:
                    ans += 1
                    last_end = r
                    break  # Greedily take the shortest valid palindrome ending first

                l -= 1
                r += 1

        return ans