import sys, timeit
start = timeit.default_timer()
lines = sys.stdin.read().splitlines() 

in_str = lines[0]
ks = lines[1]
k, l, t = map(int, ks.split(' '))


def find_str_count(cur_str, find_str):
    count = 0
    while True:

        n_start = cur_str.find(find_str)
        if n_start != -1:
            count = count + 1
            cur_str = cur_str[n_start+len(find_str):]
        else:
            break

    return count


def find_str(cur_str, find_str):
    count = 0
    k = len(find_str)
    cl = len(cur_str)
    while True:
        if cur_str[0] == find_str[0]:
            if cur_str[i:i+k] == find_str:
                count = count + 1
                cur_str = cur_str[k:]
                cl = cl - k
        else:
            cur_str = cur_str[1:]
            cl = cl-1

        if cl < k:
            break

    return count


total_length = len(in_str)
m_list = {}
start_l = 0
last_l = l - 1
max_k = 0
my_list =[]
done_list = {}

in_in_str = in_str[:l]

for i in range(0, l-k):
    c_str = in_in_str[i:i + k]
    if not done_list.get(c_str):
        c_count = in_in_str.count(c_str)
        if c_count == t:
            m_list[c_str] = t
        done_list[c_str] = c_count

# print(done_list)
for i in range(1, total_length-l+1):
    in_in_str = in_str[i:i+l]
    pre_str = in_str[i-1:i+k-1]
    c_str = in_in_str[-k:]
    if c_str == pre_str:
        pass
    else:

        if done_list.get(pre_str):
            done_list[pre_str] = done_list[pre_str] - 1
        else:
            done_list[pre_str] = 1
            print(in_in_str, i, pre_str)
        if done_list.get(c_str):
            done_list[c_str] = done_list[c_str] + 1
        else:
            done_list[c_str] = 1

        if m_list.get(c_str):
            pass
        else:
            c_count = done_list[c_str]
            if c_count == t:
                m_list[c_str] = t

print(m_list)
print(' '.join(m_list))
stop = timeit.default_timer()
print(stop-start)