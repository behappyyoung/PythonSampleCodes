def strStr(haystack, needle):
        if needle == '':
            return 0
        if haystack == '':
            return -1
        f_start = -1
        i = 0
        while i < (len(haystack) - len(needle)+1):
            if haystack[i] == needle[0]:
                f_start = i
                i += 1
                for j in range(1, len(needle)):

                    if haystack[i] != needle[j]:
                        i = f_start
                        f_start = -1
                        break
                    i += 1

                if f_start != -1:
                    return f_start
            i += 1


        return f_start

print(strStr("ippi", 'pi'))
print(strStr("A man, a plan, a canal: Panama", 'can'))