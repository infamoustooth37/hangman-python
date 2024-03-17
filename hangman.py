import random

def read_specific_line(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if 0 < line_number <= len(lines):
            return lines[line_number - 1]
        else:
            return "Line number out of range."

wordToGuess = ""
secret = ""
lives = 10
guessed = False
charFound = False
lettersGuessed = []

wordFilePath = "words.txt"
randomLine = random.randint(1,100)
wordToGuess = read_specific_line(wordFilePath,randomLine)

for i in wordToGuess:
    secret = secret + "_"

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
            print("You lost all your lives - you lose")
            print("The word was " + wordToGuess)
            break
        
