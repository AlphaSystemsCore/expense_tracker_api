from pwdlib import PasswordHash 

password_hash = PasswordHash.recommended()

DUMMY_HASH = password_hash.hash("jkrsewqqpoibvy{l..e>Mk<.\\\ljervgh7ja3};;@!")

def verify_password(plain_password, hash_password):
    return password_hash.verify(plain_password, hash_password)

def hash_password(plain_password):
    return password_hash.hash(plain_password)

