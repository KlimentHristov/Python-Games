from random import shuffle
mylist = [' ','O',' ']
# take list and return shuffle versioned
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# Create user iteraction with list
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        # recall input() returns a string
        guess = input("Pick a place, where is the magic number: 0, 1, or 2: ")
    return int(guess)

# Now we will check the user's guess. Only print here, since we have no need to save a user's guess or the shuffled list.
def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong ! Better luck next time')
        print(mylist)

# Now we create a little setup logic to run all the functions.

print(mylist)

# Shuffle It
mixedup_list = shuffle_list(mylist)

# Get User's Guess
guess = player_guess()
# Notice how this function takes in the input
# based on the output of other functions!
check_guess(mixedup_list,guess)