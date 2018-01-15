import numpy as np
import argparse
from generate_keys import list_of_primes as LoP

parser = argparse.ArgumentParser(description='solve private key with pollard rho')
parser.add_argument('e', help='public key e', type=str)
parser.add_argument('n', help='public key n', type=str)
args = parser.parse_args()

def lookupTable(n, e, list_of_primes):
    factors_dict = {a * b: [a, b] for a, b in
                    itertools.combinations(list_of_primes, 2)}
    factors = factors_dict[n]
    phi_n = phi(factors[0], factors[1])
    private_key = extendedEuler(e, phi_n)
    return private_key

if __name__ == '__main__':
    e = int(args.e)
    n = int(args.n)

    print('*Private Key d*')
    print(lookupTable(n, e, LoP))
