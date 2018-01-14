import sys 
lines = sys.stdin.read().splitlines() 

for i in range(len(lines)):
    print('Line ' + str(i+1) + ' is ' + str(len(lines[i])) + ' characters long.')
in_str = lines[0]
k = int(lines[1])


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
max = 0
r_length = len(in_str) - k
for i in range(0, r_length):
    c_str = in_str[i:i+k]
    c_count = find_str_count(in_str, c_str)
    if max <= c_count:
        max = c_count
        if m_list.get(max):
            if c_str not in m_list[max]:
                m_list[max].append(c_str)
        else:
            m_list[max] = [c_str]

print(max, m_list)
print('===>')
print(' '.join(m_list[max]))