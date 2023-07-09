import random

rand = random.randint(1,20) 

print("I am thinking of a number between 1 and 20.")

x = 0
num = 0

#print("Guess number is : ",rand) 

while num != rand:
    x += 1
    num = int(input("Take a guess number : "))
    
    if num == rand:
        print(f'Good job! You guessed my number in {x} guesses!')
        break
    elif num < rand:
        print("Your guess is too low.")
    elif num > rand:
        print("Your guess is too high.")
