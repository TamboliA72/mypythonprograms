#python word guessing game
import random
import time

#welcomming the user
print("Welcome to the Word Guessing Game")
print("Hello " + input("Enter your name: ") + " lets Play!")

time.sleep(1)

#the list of the words to guess
wordList = ["loyalty","friend","tycoon","rikshaw","state","diwali"]

#randomly generating the word to guess
word = list(random.choice(wordList))
turns = len(word) - 1
print("\nYou have " + str(turns) + " guesses")
time.sleep(1)
print("\nLets start the game.......")
time.sleep(1)
gussesWord = [0]*len(word)

#initializing the answer list
for i in range(len(gussesWord)):
    gussesWord[i] = "_ "

#checking for the answer
while turns > 0:
    flag = 0
    guess = input("\nEnter your guess: ") #getting the guess of player        
    for i in range(len(word)):        
        if guess == word[i]:            
            gussesWord[i] = guess
            flag = 1
    print("guessWord: " + ''.join(gussesWord)) #priting the guessed word!
    if flag == 0 :
        turns = turns - 1 #reducing the turns
        print("Nope. Try Again")
    if gussesWord == word:
        print("You Won!")
        break        
    print("You have " + str(turns) + " turns left!")
print("Start again to Play!")

