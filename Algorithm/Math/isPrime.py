"""
   Redo 09292019 with python3
   input :  number
   return : say if it's primer or not

## is_prime / is_prime_s : too slow

"""


"""
    
"""
def is_prime(n):
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def is_prime_s(n):
    if n<=1 or n==4:
        return False
    if n==2 or n==3:
        return True
    # Check from 2 to n/2
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False

    return True


def is_prime_s_s(n):
    if n<=1:
        return False
    if n==2 or n==3:
        return True
    # Check from 2 to n/2
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

user_int = 0

while isinstance(user_int, int):

    user_input=input("\n is prime number? : ")

    try:
        user_int = int(user_input)
    except:
        print("\n need integer input ")
        exit(1)

    from datetime import datetime
    start_time = datetime.now()
    print(is_prime_s_s(user_int))
    end_time = datetime.now()
    print(end_time - start_time)


exit(1)
