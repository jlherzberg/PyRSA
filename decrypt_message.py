import argparse

parser = argparse.ArgumentParser(description='read in message')
parser.add_argument('n', help='public key n', type=str)
parser.add_argument('d', help='private key d', type=str)
parser.add_argument('message', help='message', nargs=argparse.REMAINDER, default=[])
args = parser.parse_args()

def decrypt(encr_m, d, n):
    message = [chr(pow(int(t), d, n)) for t in encr_m]
    return ''.join(message)

if __name__ == '__main__':
    n = int(args.n)
    d = int(args.d)
    message = args.message

    print('*Decrypted Message*')
    print(decrypt(message, d, n))
