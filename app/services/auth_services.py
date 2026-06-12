from ..auths.password_handler import (hash_password, verify_password, DUMMY_HASH)
def create_user(email, password):
    hashed_password = hash_password(password)

    print(hashed_password)





#for testing
if __name__ == "__main__":
    create_user("dasf", "jkdjkj")
