##############
#   Level 1  #
# 27/03/2023 #
##############
# Create a string of prime number 235711 ...
# Given a position i, return the 5 next digits.
##############

def solution(i):
    prime = prime_list(i)
    tmp = str(prime)
    tmp2 = tmp[i:i+5]
    return tmp2

def isprime(n):
    cond = False
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n%i) == 0:
                break
        else:
            cond = True
    return cond

def prime_list(nmax):
    prime_len = 0
    num = 2
    prime = 0
    while prime_len < nmax+6:
        tmp = isprime(num)
        if tmp:
            nb_len = len(str(num))
            prime = 10**(nb_len) * prime + num
        prime_len = len(str(prime))
        num += 1
    return prime

