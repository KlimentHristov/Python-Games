import random

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("LET'S PLAY!")

num = (random.randint(1,100))
guess = int(input())
guesses = [0] # list

while guess != num:
    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS! Please try again:")
        break
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
    # if guess is incorrect, add guess to the list
    guesses.append(guess)
    if guesses[-2]:
        if abs(num-guess) < abs(num - guesses[-2]):
            print("Warmer")
        else:
            print("Colder")
    else:
        if abs(num-guess) <= 10:
            print("WARM")
        else:
            print("COLD")
    guess = int(input())
print('CONGRATULATIONS, YOU GUESSED IT!')
print(f"{len(guesses)} GUESSES!")
