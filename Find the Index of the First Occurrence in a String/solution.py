def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        else:
            # i=j=k=0

            n = len(haystack)
            m = len(needle)

            ans = -1

            for i in range(n):
                if i+m <= n :
                    if haystack[i:i+m] == needle:
                        ans = i
                        break
                else:
                    break
            return ans