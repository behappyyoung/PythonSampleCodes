import sys 
lines = sys.stdin.read().splitlines() 

in_str = lines[0]
ks = lines[1]
k, l, t = map(int, ks.split(' '))
in_str = in_str[0:l]


def find_str_count(cur_str, find_str):
    count = 0
    while True:
        n_start = cur_str.find(find_str)
        if n_start != -1 :
            count = count + 1
            cur_str = cur_str[n_start+len(find_str):]
        else:
            break
    return count


m_list = {}
r_length = l - k
for i in range(0, r_length):
    c_str = in_str[i:i+k]
    c_count = find_str_count(in_str, c_str)
    if m_list.get(c_count):
            if c_str not in m_list[c_count]:
                m_list[c_count].append(c_str)
    else:
            m_list[c_count] = [c_str]

print(m_list)
print('===>')
print(m_list[t])