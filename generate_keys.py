import numpy as np

list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                  97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

def selectTwoRandomPrimes():
    max_index = len(list_of_primes)
    a = list_of_primes[np.random.randint(max_index)]
    b = list_of_primes[np.random.randint(max_index)]
    return a, b

def phi(a, b):
    phi_a = a - 1
    phi_b = b - 1
    return phi_a * phi_b

def findGreatestCommonDivisor(a, b):
    if a == b:
        return a
    else:
        for d in range(int(min(a,b)), 0, -1):
            if a % d == 0 and b % d == 0:
                return d

def selectSmallOddInteger(n):
    e = np.random.randint(101)
    if findGreatestCommonDivisor(e, n) == 1 and \
        e % 2 == 1 and \
        e > 1:
        return e
    else:
        return selectSmallOddInteger(n)

def extendedEuler(e, phi_n, k = 1):
    d = (k * phi_n + 1) / e
    if d % 1 != 0:
        k += 1
        d = extendedEuler(e, phi_n, k)
    return int(d)

def generateAndPrintKeys():
    a, b = selectTwoRandomPrimes()
    n = a*b
    phi_n = phi(a, b)
    e = selectSmallOddInteger(n)
    d = extendedEuler(e, phi_n)
    print('*Public Keys*')
    print('n: {}'.format(n))
    print('e: {}\n'.format(e))
    print('*Private Key*')
    print('d: {}'.format(d))

if __name__ == '__main__':
    try:
        generateAndPrintKeys()
    except:
        print('Recursion Error. Try Again.')
