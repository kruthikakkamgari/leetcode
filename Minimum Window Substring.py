class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        need, window = Counter(t), {}
        have, need_len = 0, len(need)
        res, res_len = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_len:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
