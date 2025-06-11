import random

# 1. Create a list of random words
animes = ["Naruto", "Bleach", "One Piece", "Black Clover", "Kingdom", "Dr.Stone", "Blue Lock"]

# 2. Choose one word from that list randomly to be the password
password = random.choice(animes)

# 3 & 4. Print each word using a for loop and add conditionals
for word in animes:
    if word == password:
        print(word.upper())  # ✅4a: If it's the password, print it in uppercase
    else:
        print(word)          # ✅4b: Otherwise, just print it normally
