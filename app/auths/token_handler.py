from pwdlib import PasswordHash

token_hash = PasswordHash.recommended()

def hash_token(token:str):
    return token_hash.hash(token)

def verify_token(token, hashed_token):
    return token_hash.verify(token, hashed_token)
