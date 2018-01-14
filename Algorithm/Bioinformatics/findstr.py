import sys
lines = sys.stdin.read().splitlines()

for i in range(len(lines)):
    print('Line ' + str(i+1) + ' is ' + str(len(lines[i])) + ' characters long.')
in_str = lines[0]
find_str = lines[1]

print(in_str.find(find_str))
count = 0
while True:
    n_start = in_str.find(find_str)
    if n_start != -1:
        count = count + 1
        in_str = in_str[n_start+len(find_str):]
    else:
        break
print(count)