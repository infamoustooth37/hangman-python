wordToGuess = input("Enter a word to guess ")
secret = ""
lives = 5
guessed = False
charFound = False

for i in wordToGuess:
    secret = secret + "-"

print(secret)

letters = len(wordToGuess)
while guessed == False:
    charFound = False
    charGuessed = input ("Enter a letter to guess ")
    if charGuessed != " " and charGuessed != "":
        for i in range(len(wordToGuess)):
            if wordToGuess[i] == charGuessed:
                secret = secret[:i] + charGuessed + secret[i+1:]
                charFound = True
                letters -= 1
        if charFound == False:
            print(charGuessed + " Is not a character in the secret word - you lost a life")
            lives -= 1
        print(secret)
        print("Lives: " + str(lives))
        if letters == 0:
            print("you guessed the word correctly!")
            print("The word was " + secret)
            guessed = True
        if lives <= 0:
            print("You lost all your lives - you lost")
            break
        