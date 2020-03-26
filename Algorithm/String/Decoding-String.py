"""
s = 3[a]2[bc]
=> aaabcbc

s=3[a2[c]]xy
==> accaccaccxy

"""

def decoding_string(s):
    int_stack = list()
    char_stack = list()
    i = 0
    t_str = ''
    while i < len(s):
        if s[i].isdigit():
            if s[i+1].isdigit():
                int_stack.append(int(s[i]+s[i+1]))
                i += 1
            else:
                int_stack.append(int(s[i]))
        else:
            if s[i] == ']':
                ctop = char_stack.pop()
                while ctop != '[':
                    t_str = ctop + t_str
                    ctop = char_stack.pop()
                c_int = int_stack.pop()
                m_str = ''
                for j in range(c_int):
                    m_str += t_str
                char_stack.append(m_str)
                t_str = ''
            else:
                char_stack.append(s[i])

        i += 1

    while char_stack:
        ctop = char_stack.pop()
        t_str = ctop + t_str
    return t_str

s = '3[a]2[bc]'
print(decoding_string(s))
s='3[a2[c]]xy'
print(decoding_string(s))