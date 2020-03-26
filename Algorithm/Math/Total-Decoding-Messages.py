"""
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given encoded message "123",
it could be decoded as "ABC" (1 2 3) or "LC" (12 3) or "AW"(1 23).
So total ways are 3.

"""

def total_decoding(ds):
    count = [0] * (len(ds)+1)
    count[0] = 1

    for i in range(1, len(ds)):
        if ds[i-1] == '1' or (ds[i-1] == '2' and int(ds[i]) <= 7):
            count[i] = 2
        else:
            count[i] = 1
    total_count = 0
    for i in count:
        total_count += i

    total_count = total_count if ds[-1] != 0 else total_count -1

    return total_count


input_str = '2424'

print(total_decoding(input_str))