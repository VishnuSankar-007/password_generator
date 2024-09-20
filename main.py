
import random
import string
import hashlib
import os

# Algorithm 1: Basic Random Character Selection
def basic_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Algorithm 2: Passphrase Generator (Diceware Method)
def passphrase_generator(word_count=4):
    word_list = ["apple", "orange", "banana", "grape", "lemon", "strawberry", "peach", "melon", "kiwi", "mango"]
    passphrase = '-'.join(random.choice(word_list) for i in range(word_count))
    return passphrase

# Algorithm 3: Pattern-based Password (Combination of Words and Numbers)
def pattern_based_password():
    word_list = ["sky", "blue", "tree", "mountain", "river"]
    random_word = random.choice(word_list)
    number = ''.join(random.choice(string.digits) for i in range(3))
    special_char = random.choice(string.punctuation)
    password = random_word.capitalize() + number + special_char
    return password

# Algorithm 4: Entropy-based Password (Secure Hash with Salt)
def entropy_based_password(length=12):
    salt = os.urandom(16)
    random_data = os.urandom(16)
    hash_value = hashlib.sha256(salt + random_data).hexdigest()[:length]
    return hash_value

# Testing all password generators
if __name__ == "__main__":
    print("Basic Random Password:", basic_random_password())
    print("Passphrase Password:", passphrase_generator())
    print("Pattern-based Password:", pattern_based_password())
    print("Entropy-based Password:", entropy_based_password())


