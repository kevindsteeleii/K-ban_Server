import bcrypt

def hash_password(password):
    password = password.encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed

def verify_login(hashed, password):
    password = password.encode()
    return bcrypt.checkpw(password, hashed)

if __name__ == '__main__':
    salt = 'salt'
    right_pass = 'password'
    wrong_pass = 'wrong password'

    hashed_word = hash_password(right_pass)
    print(hashed_word)
    pass_right_test = verify_login(hashed_word, right_pass)

    print(pass_right_test)
    print(verify_login(hashed_word, wrong_pass))
