# PyRSA

## Encrypt messages to your friends with python and RSA!

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

\*Only [A-Za-z] characters

## Update: Now intercept and decrypt your friends' messages too!

Instructions

1. Repeat as above

2. Obtain **public** keys and the encrypted message

3. Choose your solving method. Currently there are two options.
 - A look up table
 - Pollard's Rho algorithm

4. To solve with the lookup table, you will also need a list of primes at least
as large as that which your friends used. Currently, it imports from the generate_keys.py file. Then run lookup_table.py.

    `python lookup_table.py <public key e> <public key n>`

5. TO solve with the Pollard Rho algorithm, simply run pollard_rho.py

    `python pollard_rho.py <public key e> <public key n>`
