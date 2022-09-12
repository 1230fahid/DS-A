class Solution:
    def lengthOfLongestSubstring_my_solution(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        tup = ()
        tup += (s[0],)
        arr = [1]
        i = 1
        while i < len(s):
            if(s[i] in tup):
                if(len(tup) > arr[0]):
                    arr[0] = len(tup)
                i = i-len(tup) + 1
                tup = ()
                tup += (s[i],)
            else:
                tup += (s[i],)
            i+=1
    
        if(len(tup) > arr[0]):
            arr[0] = len(tup)
        return arr[0]
    
    def lengthOfLongestSubstring_optimized(self, s:str) -> int:
        last_idx = {}
        max_len = 0

        # starting index of current
        # window to calculate max_len
        start_idx = 0

        for i in range(0, len(s)):

            # Find the last index of str[i]
            # Update start_idx (starting index of current window)
            # as maximum of current value of start_idx and last
            # index plus 1
            if s[i] in last_idx:
                start_idx = max(start_idx, last_idx[s[i]] + 1)

            # Update result if we get a larger window
            max_len = max(max_len, i-start_idx + 1)

            # Update last index of current char.
            last_idx[s[i]] = i

        return max_len
