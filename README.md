# PyRSA

Encrypt messages to your friends with python and RSA!

Instructions

1. Download the repo

  `git clone https://github.com/jherzberg/PyRSA.git`

2. Run generate_keys.py in the command line

  `python generate_keys.py`

3. Give your friend your **public** keys

4. Your friend runs encrypt_message.py with your public keys and their message*

  `python encrypt_message.py <public key e> <public key n> 'hello world'`

5. Your friend gives you the encrypted message

6. Run decrypt message with your private keys

  `python decrypt_message.py <public key n> <private key d> <encrypted message>`

*Only [A-Za-z] characters
