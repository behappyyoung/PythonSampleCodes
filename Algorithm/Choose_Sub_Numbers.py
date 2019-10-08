
def sub_num(num, count):        #width self
	# print 'num :' , num, 'count :', count
	if num == count:
		nums = []
		for i in range(1, num + 1):
			nums.append(str(i))
		return [','.join(nums)]
	elif count == 1:
		nums = []
		for i in range(1, num+1):
			nums.append(i)
		return nums
	elif count > num :
		return False

	if num >= count:
		sub1 = sub_num(num - 1, count - 1)
		if isinstance(sub1, str):
			sub1 = [str(num) + ',  ' +sub1]
		else:
			subsub = []
			for i in sub1:
				subsub.append(str(i) + ',' + str(num))
			sub1 = subsub
	else:
		sub1 = []
	return sub1



def get_subs(num, count):
	for i in range(num, count-1, -1):
		subs = sub_num(i, count)
		print(i, count, subs)
		for i in subs:
			print(i)

get_subs(4, 2)