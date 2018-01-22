import timeit
start = timeit.default_timer()
file = open('E_coli.txt', 'r')

# 9-mer , (500, 3)
k = 9
t = 3
l = 500
file_text = file.read()

total_length = len(file_text)
m_list = {}
start_l = 0
last_l = l - 1
max_k = 0
my_list =[]
done_list = {}

in_in_str = file_text[:l]

for i in range(0, l-k):
    c_str = in_in_str[i:i + k]
    if not done_list.get(c_str) and not m_list.get(c_str):
        c_count = in_in_str.count(c_str)
        if c_count == t:
            m_list[c_str] = t
        done_list[c_str] = c_count

# print(done_list)
for i in range(1, total_length-l):
    in_in_str = file_text[i:i+l]
    pre_str = file_text[i-1:i+k-1]
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

print(len(m_list))
# print(' '.join(m_list))
stop = timeit.default_timer()
print(stop-start)
