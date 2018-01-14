import sys
lines = sys.stdin.read().splitlines()

find_str = lines[0]
in_str = lines[1]
positions = []
last_found =0
while True:
    n_start = in_str.find(find_str)
    if n_start != -1:
        last_found = n_start + last_found
        positions.append(str(last_found))
        in_str = in_str[n_start+1:]
        last_found = last_found + 1
    else:
        break
print(' '.join(positions))