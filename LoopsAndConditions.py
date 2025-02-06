# James Aho
# LoopsAndConditions.py
# This program covers 4.1, 4.2, 6.1, 6.2, 6.3 questions from the book.

# ===================================== Question 4.1 =====================================

secret = 4
guess = float(input("Choose a number between 1 and 10"))

if guess > secret:
    print("too high")

elif guess < secret:
    print("too low")

else:
    print("just right")

# ===================================== Question 4.2 =====================================

small = True
green = False

if small == True:
    if green == True:
        print("Pea")
    else:
        print("Cherry")
    
else:
    if green == True:
        print("Watermelon")
    else:
        print("Pumpkin")

# ===================================== Question 6.1 =====================================

TacoBell = [3,2,1,0]

for i in TacoBell:
    print(i)

# ===================================== Question 6.2 =====================================

guess_me = 7

number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number > guess_me:
        print("oops")
        break
    else:
        print("found it!")
        break
    number += 1

# ===================================== Question 6.3 =====================================

guess_me = 5

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number > guess_me:
        print("oops")
        break
    else:
        print("found it!")
        break
