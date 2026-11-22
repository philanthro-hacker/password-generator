import random
import string

length = int(input("How long should the password be? "))
use_symbols = input("Include symbols? (y/n): ").lower() == "y"
count = int(input("How many passwords do you want? "))

chars = string.ascii_letters + string.digits
if use_symbols:
    chars += "!@#$%^&*"

def strength(pw):
    if len(pw) < 8:
        return "Weak 😟"
    elif len(pw) < 12:
        return "Good 🙂"
    elif use_symbols:
        return "Strong 💪"
    else:
        return "Good 🙂"

print("\n--- Your passwords ---")
for i in range(count):
    password = "".join(random.choice(chars) for _ in range(length))
    print(f"{i+1}. {password}  -> {strength(password)}")
