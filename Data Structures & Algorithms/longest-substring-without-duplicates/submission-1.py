class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()          # Stores unique characters in the current window
        l = 0                    # Left pointer of the sliding window
        res = 0                  # Length of the longest valid substring found

        for r in range(0, len(s)):   # Expand the window by moving the right pointer
            while s[r] in charSet:   # If duplicate found, shrink window until it's removed
                charSet.remove(s[l]) # Remove the leftmost character from the set
                l += 1               # Move the left pointer to the right
            charSet.add(s[r])        # Add the current character to the window
            res = max(res, r - l + 1) # Update the maximum window size
        return res                   # Return the length of the longest substring