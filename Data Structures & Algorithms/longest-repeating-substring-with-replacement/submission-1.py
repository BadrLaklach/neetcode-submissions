class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0                   # Length of the longest valid substring found
        count = {}                # Stores the frequency of each character in the current window
        l = 0                     # Left pointer of the sliding window

        for r in range(len(s)):   # Expand the window by moving the right pointer
            count[s[r]] = 1 + count.get(s[r], 0)  # Increment frequency of the current character

            while (r - l + 1) - max(count.values()) > k:  # If replacements needed exceed k
                count[s[l]] -= 1      # Remove the leftmost character from the window
                l += 1                # Move the left pointer to the right

            res = max(res, r - l + 1) # Update the maximum valid window size

        return res                    # Return the length of the longest valid substring