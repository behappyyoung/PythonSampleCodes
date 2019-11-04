"""
   Redo 09292019 with python3
   input :  integer
   return : list of prime number equal or less than input number
"""
user_input=input("\n Generate prime numbers up to what number? : ")

try:
    user_int = int(user_input)
except:
    print("\n need integer input ")
    exit(1)

"""
    without math
"""


def isPrime(n):
    if n<=1 or n==4:
        return False
    if n==2 or n==3:
        return True
    # Check from 2 to n/2
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

def get_primer_list(i_number):
    primber_list = []
    if i_number <= 1:
        return primber_list
    for i in range(2, i_number+1):
        if isPrime(i):
            primber_list.append(i)
    return primber_list

"""
    with math
"""
def get_primer_list_s(i_number):
    # Corner case
    if i_number < 2:
        return []
    if i_number == 2:
        return [2]
    if i_number == 3:
        return [2, 3]

    import math

    current_number=3
    primber_list=[2, 3]

    while current_number < (i_number-1):
        current_number += 2
        test = True
        sqrt_current_number = math.sqrt(current_number)
        for a in primber_list:
            if a > sqrt_current_number:
                break
            if current_number % a == 0:
                test=False
                break
        if test:
            primber_list.append(current_number)
    return primber_list

print('primers : %s' % get_primer_list(user_int))
print('primers : %s' % get_primer_list_s(user_int))