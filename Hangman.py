import random
from kalamat import kalamat
from scaffold import print_scaffold


# Create a list for choose from it randomely
list = kalamat


# choose a random var from list
randomChoose = random.choice(list)

# lives
lives = 0

# print a list of "_" for the len of our random choice
emptyList = []
for i in range(len(randomChoose)):
    emptyList.append("_")
print(emptyList)

endOfTheGame = False

while not endOfTheGame:
    # get a char from user

    guess = input("character ro type kon: ").lower()

    if guess in emptyList:
        print(f"{guess} ro  ghablan gofte boodi!!!!!!!!")

    # check if input char is excist in randomchoice
    for i in range(len(randomChoose)):
        letter = randomChoose[i]
        if letter == guess:
            emptyList[i] = letter

    if guess not in randomChoose:
        lives += 1
        print("oh oh in ke nabood")

    print(emptyList)
    print_scaffold(lives)

    if lives == 6:
        print(
            f":D :D  hahahahahha!!!!!natoonesti ke........kalameye dorost in bood ========> {randomChoose.upper()}")
        break

    if "_" not in emptyList:
        endOfTheGame = True
        print(f"baba barikala to bordi ".capitalize())
