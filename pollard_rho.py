import numpy as np
import argparse

parser = argparse.ArgumentParser(
    description='solve private key with pollard rho')
parser.add_argument('e', help='public key e', type=str)
parser.add_argument('n', help='public key n', type=str)
args = parser.parse_args()


def findGreatestCommonDivisor(a, b):
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b % a, a
    return b


def pollardRho(n):
    x, c = np.random.randint(1, n - 1), np.random.randint(1, n - 1)
    y = x

    def f(g, b):
        return g**2 + b
    x = f(x, c)
    y = f(f(y, c), c)
    if findGreatestCommonDivisor(abs(x - y), n) == 1:
        return pollardRho(n)
    else:
        return findGreatestCommonDivisor(abs(x - y), n)


def keysPollardRho(n, e):
    factor = pollardRho(n)
    other_factor = n / factor
    phi_n = phi(factor, other_factor)
    private_key = extendedEuler(e, phi_n)
    return private_key


if __name__ == '__main__':
    e = int(args.e)
    n = int(args.n)

    print('*Private Key d*')
    print(keysPollardRho(n, e))
