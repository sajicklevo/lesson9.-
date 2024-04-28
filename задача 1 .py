
import string
import secrets

def random_string(length):
    letters = string.ascii_letters
    return ''.join(secrets.choice(letters) for _ in range(length))
print(random_string(10))