import string
from random import sample

def get_random_password(n = 8) -> str:
    password = sample(string.ascii_letters + string.digits, n)
    return "".join(password)


print(get_random_password())
