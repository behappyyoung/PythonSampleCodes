'''
4
add hack
add hackerrank
find hac
find hak

2
0

5
add hack
add hackerrank
add hacker
find hac
find hak

'''
n = int(raw_input().strip())


mytrie = {}
found = []


def add_name(word):
	temp_trie = mytrie
	for letter in word:
		if letter in temp_trie:
			temp_trie = temp_trie[letter]
			temp_trie['count'] += 1
		else:
			temp_trie = temp_trie.setdefault(letter, {'count': 1})
	temp_trie = temp_trie.setdefault('_end_', '_end_')


def find_partial(word):
	word_index = 0
	letter_count = 0
	word_length = len(word)
	temp_trie = mytrie
	for letter in word:
		if letter in temp_trie:
			if word_index == word_length - 1:
				letter_count = temp_trie[letter]['count']
			else:
				temp_trie = temp_trie[letter]
				word_index += 1
		else:
			return letter_count

	return letter_count


for a0 in xrange(n):
	op, contact = raw_input().strip().split(' ')
	if op == 'add':
		add_name(contact)
	else:
		found.append(find_partial(contact))

for l in found:
	print l


