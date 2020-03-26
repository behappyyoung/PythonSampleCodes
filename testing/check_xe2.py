from sys import argv
first, second = argv
file_name = second + '.py'
with open(file_name) as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print(i, repr(line))
