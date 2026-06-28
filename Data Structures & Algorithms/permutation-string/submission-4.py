class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False   # Impossible if s1 is longer than s2

        s1Count, s2Count = [0] * 26, [0] * 26  # Frequency arrays for s1 and current window in s2

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1  # Count characters in s1
            s2Count[ord(s2[i]) - ord('a')] += 1  # Count characters in the first window of s2

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)  # Count how many character frequencies match

        l = 0
        for r in range(len(s1), len(s2)):   # Slide the window through s2
            if matches == 26: return True   # All 26 character counts match → permutation found

            index = ord(s2[r]) - ord('a')   # Index of the new character entering the window
            s2Count[index] += 1             # Add it to the window frequency

            if s1Count[index] == s2Count[index]:
                matches += 1                # Counts became equal
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1                # Counts were equal but now differ by adding one extra

            index = ord(s2[l]) - ord('a')   # Index of the character leaving the window
            s2Count[index] -= 1             # Remove it from the window frequency

            if s1Count[index] == s2Count[index]:
                matches += 1                # Counts became equal again
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1                # Counts were equal but now differ after removing one

            l += 1                          # Move the left pointer

        return matches == 26                # Check the final window