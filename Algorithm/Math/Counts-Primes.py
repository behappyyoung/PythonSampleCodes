"""
   Redo 09292019 with python3
   input :  number
   return : say if it's primer or not

## is_prime / is_prime_s : too slow

"""


"""
Count the number of prime numbers less than a non-negative number, n.


   Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
 
"""
def countPrimes(n):
        prime_list = list()
        def isPrime(n):
            if n <= 1:
                return False
            elif n == 2 or n == 3:
                return True
            else:
                for p in prime_list:
                    if n % p == 0:
                        return False
                return True
        count = 0
        for i in range(2, int(n/2)):
            if isPrime(i):
                prime_list.append(i)
                count += 1
        for j in range(int(n/2), n):
            p = True
            for p in prime_list:
                if j % p == 0:
                    p = False
                    break
                p = True
            if p:
                count += 1
        return count


def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    count = 0
    for p in range(2, n):
        if prime[p]:
            # print(p)
            count += 1
    print(count)


if __name__ == '__main__':
    n = 999983
    # print("Following are the prime numbers smaller","than or equal to", n)
    SieveOfEratosthenes(n)

