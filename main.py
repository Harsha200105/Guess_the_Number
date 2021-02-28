import random
randNumber = random.randint(1,100)
#print(randNumber)
Guesses = 0
userGuess = None

while (userGuess != randNumber):
    userGuess =int(input("Enter your guess: "))
    Guesses += 1
    if (userGuess==randNumber):
        print("Congratulations you guessed it right!!")

    else:
        if (userGuess<randNumber):
            print("You guessed it wrong\nEnter a bigger number")

        else:
            print("You guessed it wrong\nEnter a smaller number")

print(f"You took {Guesses} guesses")
with open('bigScore.txt','r')as f:
    bigScore = int(f.read())

if Guesses<bigScore :
    with open('bigScore.txt', 'w') as f:
        f.write(str(Guesses))
