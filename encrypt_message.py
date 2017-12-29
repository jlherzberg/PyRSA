import argparse

parser = argparse.ArgumentParser(description='read in message')
parser.add_argument('n', help='public key n', type=str)
parser.add_argument('e', help='public key e', type=str)
parser.add_argument('message', help='message', type=str)
args = parser.parse_args()

def encrypt(m, e, n):
    message = [ord(i) for i in list(m)]
    return ' '.join([str(pow(j, e, n)) for j in message])

if __name__ == '__main__':
    e = int(args.e)
    n = int(args.n)
    message = str(args.message)

    print('*Encrypted Message*')
    print(encrypt(message, e, n))
