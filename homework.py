import random
import string

def generate_random_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    print(random.choice(chars))
    return''.join(random.choice(chars) for _ in range(length))

if __name__ == '__main__':
    password = generate_random_password(5
                                        )
    print('Random password:', password)
