class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        window_start= window_end= 0
        seen= set()
        max_len= 0

        for window_end in range(len(s)):

            while s[window_end] in seen:
                seen.remove(s[window_start])
                window_start+= 1

            seen.add(s[window_end])
            max_len= max(max_len, len(seen))
        return max_len
            

