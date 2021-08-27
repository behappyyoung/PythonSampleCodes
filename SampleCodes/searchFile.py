from sys import argv
script, filename = argv
import re

dict = {}

with open(filename) as f:
	
	for line in f:
		print(line)
		m = re.search('add key="(/.*)" value="(.*)"', line)
		if m:
			print(m.group(0))
			m1 = m.group(1)
			m2 = m.group(2)
			if m2 != 'y':
				print(type(m1), m1, m2)
				dict[m1] = m2

##print dict


