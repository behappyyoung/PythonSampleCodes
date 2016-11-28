# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M, K = map(int,raw_input().split())

fishes ={}

for i in xrange(N):
    fish = map(int, raw_input().split())
    fishes[i] =[]
    for f in xrange(1, fish[0]+1):
        fishes[i].append(fish[f])

print fishes
min_shopping = []


loads ={}

for i in xrange(M):
    load_from, load_to, t_time = map(int, raw_input().split())
    if load_to in loads:
        loads[load_to].append({'load_from': load_from, 't_time' : t_time})
    else:
        loads[load_to] = [{'load_from': load_from, 't_time' : t_time}]

print loads
pathes =[]


def getPath(obj, start):
    path = str(start)
    if start not in obj:
        return path
    else:
        for i in xrange(len(obj[start])):
            path += str(getPath(obj, obj[start][i]['load_from']))
            print i
    return path

print getPath(loads, N)
result = 0
# Compute the final result using the inputs from above

print result