class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If t is empty, no window is needed
        if t == "":
            return ""

        countT, window = {}, {}

        # Count the frequency of each character in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have = number of characters whose required frequency is satisfied
        # need = total number of unique characters we must satisfy
        have, need = 0, len(countT)

        # Store the best window [left, right] and its length
        res, resLen = [-1, -1], float("infinity")

        # Left pointer of the sliding window
        l = 0

        # Expand the window by moving the right pointer
        for r in range(len(s)):
            c = s[r]

            # Add current character to the window
            window[c] = 1 + window.get(c, 0)

            # If this character now meets its required frequency, increment have
            if c in countT and window[c] == countT[c]:
                have += 1

            # Try to shrink the window while it remains valid
            while have == need:

                # Update the smallest valid window found so far
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Remove the leftmost character from the window
                window[s[l]] -= 1

                # If removing it makes the window invalid, decrement have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # Move the left pointer to continue shrinking
                l += 1

        # Extract the best window indices
        l, r = res

        # Return the minimum window if one exists, otherwise an empty string
        return s[l : r + 1] if resLen != float("infinity") else ""