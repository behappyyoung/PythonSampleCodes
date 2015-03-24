# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    
    answer = 0
    # write code to compute answer
    buy = int(A / B)
    wrapper = buy
    answer = buy
    while wrapper >= C1:
        extra = int(wrapper / C1)
        remain = int(wrapper % C1)
        wrapper = remain + extra       
        answer = answer + extra
    print answer

