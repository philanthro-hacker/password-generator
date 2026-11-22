import random
import string

length = int(input("How long should the password be? "))
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

chars = string.ascii_letters + string.digits
if use_symbols:
    chars += "!@#$%^&*"

password = "".join(random.choice(chars) for _ in range(length))
print(f"\nYour password: {password}")
