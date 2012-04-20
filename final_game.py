# File: final_game.py
# Date: 22 April 2009
# Created by: Lara Pollack
# Assignment: 7

from myro import *
from random import *
from sys import *
y = 1
n = 0
Y = 1
N = 0
items = []
def intro():#gives rules and gameplay
    print "Before we begin, please note that due to temporal irregularites, all word answers must be given in quotation marks."
    print "Welcome to Castle Improbable, traveller."
    print "In this game, you will explore a castle.  To move through the rooms, you must complete a task.  At the end of the game, you will see an inventory of items you have collected."
    moveOn = input("Press any numerical key then enter when ready to proceed.")

def gameover():
    print "GAME OVER"
    print "Thank you for playing Castle Improbable"
    print "You have obtained the following items:", items
    print "Please come again soon."
    sys.exit("Thank you for playing") #I know that this forces an error, but it's the only thing I tried that gets me out of the program
    gameOver = True
    return gameOver
    
def leftChoice0():
    print "You walk up to the LEFT DOOR."
    print "There is a riddle posted on it."
    print "The riddle reads: 'The beginning of eternity, the end of time and space.  The beginning of every end, and the end of everyplace.  Who am I?'"
    answer = input("What is the answer to the riddle?")
    if answer == "e" or answer == "E" or answer == "the letter e" or answer == "the letter E" or answer == "the letter 'e'" or answer == "the letter 'E'":
        print "Congratulations, you got an EGG."
        item = "EGG"
        items.append(item)
        print "You walk into the next room."
    
def rightChoice0():
    print "You walk up to the RIGHT DOOR."
    print "A GENIE appears.  He will give you a LAMP if you can guess how many wishes it contains, a number between 1 and 10.  You have 5 guesses."
    print "Please note that answers in this room should not be in quotation marks."
    genieNumber = randint(1, 10)
    for i in range(5):
        guess = input("How many wishes does the lamp have? ")
        if genieNumber == guess: 
            print "Yes, that is the correct number of wishes.  Congratulations, you got a LAMP."
            item = "LAMP"
            items.append(item)
            print "You walk into the next room."
            break
        elif genieNumber > guess:
            print "No, it has more than that."
        else:
            print "No, it doesn't have that many."
        
def room0():
	nextRoom = False
	while not nextRoom:
                print "Welcome to Castle Improbable."
		print "You appear to be standing in the FOYER"
		choiceValid = False
		print "There are two exits to this room, RIGHT and LEFT."
		while not choiceValid:
			choice = str(input("Which door do you want to try?"))
			if choice == "left" or choice == "LEFT" or choice == "Left":
				choiceValid = True
				leftChoice0()
				nextRoom = True
			elif choice == "right" or choice == "RIGHT" or choice == "Right":
				choiceValid = True
				rightChoice0()
				nextRoom = True
			else:
                            print "That is not an exit.  Please try again."

def leftChoice1():
    print "You walk up to the left door."
    print "A SERVING MAN appears to block your way."
    print "He needs help with his math homework.  Answer the following simple questions to move on."
    question1= input("3*5=")
    if question1 == 15 or question1 == "15":
        print "Correct!"
    else:
        print "Incorrect."
    question2 = input("5*6=")
    if question2 == 30 or question2 == "30":
        print "Correct!"
    else:
        print "Incorrect."
    question3 = input("7*8=")
    if question3 == 56 or question3 == "56":
        print "Correct!"
    else:
        print "Incorrect."
    question4 = input("4*9=")
    if question4 == 36 or question4 == "36":
        print "Correct!"
    else:
        print "Incorrect."
    question5 = input("2*8=")
    if question5 == 16 or question5 == "16":
        print "Correct!"
    else:
        print "Incorrect."
    print "Congratulations, you got a RUBBER CHICKEN."
    item = "RUBBER CHICKEN"
    items.append(item)
    print "You walk into the next room."

def rightChoice1():
    print "You walk up to the RIGHT DOOR."
    print "A SERVING MAN appears.  He is clearing dinner dishes.  He asks you to help."
    choice = input("Do you? (y/n)")
    if choice == y or choice == Y or choice == "y" or choice == "Y":
        print "You help him.  He is grateful and gives you a leftover PIECE OF CHICKEN."
        item = "PIECE OF CHICKEN"
        items.append(item)
    else:
        print "He bashes you over the head with the SERVING TRAY."
        gameover()
        gameOver = True
        return gameOver
    print "You walk into the next room."
    
def room1():
	nextRoom = False
	while not nextRoom:
		print "You have entered the BANQUET HALL"
		choiceValid = False
		print "There are two exits to this room, RIGHT and LEFT."
		while not choiceValid:
			choice = str(input("Which door do you want to try?"))
			if choice == "left" or choice == "LEFT" or choice == "Left":
				choiceValid = True
				leftChoice1()
				nextRoom = True
			elif choice == "right" or choice == "RIGHT" or choice == "Right":
				choiceValid = True
				rightChoice1()
				nextRoom = True
			else:
                            print "That is not an exit.  Please try again."
def leftChoice2():
    print "You walk up to the LEFT DOOR."
    print "The exit is guarded by the SPIT DOGS.  They look hungry and angry."
    choice = input("Do you have a PIECE OF CHICKEN to feed them with? (y/n)")
    if choice == y:
        print "You feed the dogs."
        items.remove("PIECE OF CHICKEN")
        print "You walk into the next room."
    else:
        print "Since you don't have anything to feed the dogs with, the dogs eat you instead."
        gameover()
        gameOver = True
        return gameOver

def rightChoice2():
    print "You walk up to the RIGHT DOOR."
    print "You encounter a COOK."
    print "He asks you, 'To what film was the Oscar for Best Picture awarded in 1939?'"
    answer = input("What do you tell him?")
    if answer == "Gone With the Wind" or answer == "gone with the wind" or answer == "GONE WITH THE WIND" or answer == "Gone With The Wind" or answer == "Gone with the wind" or answer == "Gone with the Wind":
        print "Congratulations, that was the correct answer."
        print "You get a set of CURTAINS."
        item = "CURTAINS"
        items.append(item)
        print "You walk into the next room."

def room2():
	nextRoom = False
	while not nextRoom:
		print "You are in the KITCHEN"
		choiceValid = False
		print "There are two exits to this room, RIGHT and LEFT."
		while not choiceValid:
			choice = str(input("Which door do you want to try?"))
			if choice == "left" or choice == "LEFT" or choice == "Left":
				choiceValid = True
				leftChoice2()
				nextRoom = True
			elif choice == "right" or choice == "RIGHT" or choice == "Right":
				choiceValid = True
				rightChoice2()
				nextRoom = True
			else:
                            print "That is not an exit.  Please try again."
def leftChoice3():
    print "You walk up to the LEFT DOOR."
    print "The door is blocked by a SPHINX."
    print "She asks you the following riddle: 'What has four legs in the morning, two legs at midday, and three legs in the evening?'"
    answer = input("What is the answer to her riddle?")
    if answer == "man" or answer == "a man" or answer == "MAN" or answer == "A MAN" or answer == "A man":
        print "Your answer was correct."
        print "She lets you pass, but not before giving you a SCAR."
        item = "SCAR"
        items.append(item)
        print "You walk into the next room."
    else:
        print "That was not the correct answer to the riddle."
        print "She kills you."
        gameover()
        gameOver = True
        return gameOver

def rightChoice3():
    print "You walk up to the RIGHT DOOR."
    print "You encounter ELVIS."
    print "He bets you a FLUFFERNUTTER SANDWICH that he can guess the number between 1 and 10 you're thinking of in 5 guesses."
    ready = input("Please think of a number, and press any numeric key when ready. Please note that answers in this room should not be in quotation marks.")
    x = 1
    y = 10
    for i in range(5):
        elvisGuess = (x+y)/2
        print "Elvis guesses", elvisGuess
        response = input("Please enter 0 if his guess is correct, 1 if his guess is too high, and -1 if his guess is too low.")
        if response == 0:    
            print "Congratulations, you got a FLUFFERNUTTER SANDWICH."
            item = "FLUFFERNUTTER SANDWICH"
            items.append(item)
            print "You walk into the next room."
            break
        elif response == -1:
            x = elvisGuess
        else:
            y = elvisGuess

def room3():
	nextRoom = False
	while not nextRoom:
		print "You enter the HALLWAY."
		choiceValid = False
		print "There are two exits to this room, RIGHT and LEFT."
		while not choiceValid:
			choice = str(input("Which door do you want to try?"))
			if choice == "left" or choice == "LEFT" or choice == "Left":
				choiceValid = True
				leftChoice3()
				nextRoom = True
			elif choice == "right" or choice == "RIGHT" or choice == "Right":
				choiceValid = True
				rightChoice3()
				nextRoom = True
			else:
                            print "That is not an exit.  Please try again."
def leftChoice4():
    print "You walk up to the LEFT DOOR."
    print "You encounter the LADY OF THE HOUSE."
    print "She asks, 'What do I have in my pocket?"
    answer = input("What does she have in her pocket?")
    if answer == "ring" or answer == "a ring" or answer == "RING" or answer == "A RING" or answer == "Ring" or answer == "A Ring" or answer == "the ring" or answer == "THE RING" or answer == "The Ring":
        print "Congratulations, that was the correct answer."
        print "She gives you the RING.  (You might want to wait before you put it on)"
        item = "RING"
        items.append(item)
        print "You walk into the next room."
    else:
        print "Sorry, that's not it."
def rightChoice4():
    print "You walk up to the RIGHT DOOR."
    print "You encounter the LORD OF THE HOUSE."
    print "He accuses you of cheating with his wife, and challenges you to a duel."
    print "You will both select a number between 1 and 10.  Whoever has the highest number this turn wins a point.  The duel is to three."
    hisCounter = 0
    yourCounter = 0
    while hisCounter != 3 and yourCounter != 3:
        hisNumber = randint(1, 10)
        yourNumber = input("What is your number?")
        print "His number is", hisNumber
        if hisNumber == yourNumber:
            print "This round is a tie.  Neither player got a point."
        elif hisNumber > yourNumber:
            print "He won this round."
            hisCounter = hisCounter + 1
        else:
            print "You won this round."
            yourCounter = yourCounter + 1
    if yourCounter == 3:
            print "Congratulations, you have won the duel."
            print "You take his SEVERED HEAD as a trophy."
            item = "SEVERED HEAD"
            items.append(item)
            print "You walk into the next room."
    else:
            print "You lost the duel."
            print "The lord of the house killed you in a fit of jealous rage."
            gameover()
            gameOver = True
            return gameOver

def room4():
	nextRoom = False
	while not nextRoom:
		print "You find yourself in the MASTER BEDROOM."
		choiceValid = False
		print "There are two exits to this room, RIGHT and LEFT."
		while not choiceValid:
			choice = str(input("Which door do you want to try?"))
			if choice == "left" or choice == "Left" or choice == "LEFT":
				choiceValid = True
				leftChoice4()
				nextRoom = True
			elif choice == "right" or choice == "RIGHT" or choice == "Right":
				choiceValid = True
				rightChoice4()
				nextRoom = True
			else:
                            print "That is not an exit.  Please try again."
def leftChoice5():
    print "You walk up to the LEFT DOOR."
    print "You encounter VOLDEMORT!"
    live = input("Do you have a SCAR? (y/n)")
    if live == n or live == "n" or live == "N":
        print "The last thing you hear is a voice shouting 'Avada Kedavra!'  Then everything goes black."
        gameover()
        gameOver = True
        return gameOver
    else:
        print "VOLDEMORT shouts 'Avada Kedavra!'  However, the curse rebounds off your scar and kills VOLDEMORT."
        print "Congratulations, you have killed the Dark Lord. You are the traveller who lived.  Please take the ELDER WAND."
        item = "ELDER WAND"
        items.append(item)
        print "You walk into the next room."
def rightChoice5():
    print "You walk up to the RIGHT DOOR."
    print "You encounter a MOUSE."
    print "It asks you the answer to life, the universe, and everything."
    answer = input("What do you tell it?")
    if answer == 42 or answer == "42":
        print "That was the correct answer."
        print "The MOUSE gives you a TOWEL."
        item = "TOWEL"
        items.append(item)
        print "You walk into the next room."
    else:
        print "That was not the correct answer."
        print "VOGONS just destroyed Castle Improbable."
        gameover()
        gameOver = True
        return gameOver

    
def room5():
	nextRoom = False
	while not nextRoom:
		print "You find yourself in an EMPTY ROOM."
		choiceValid = False
		print "There are two exits to this room, RIGHT and LEFT."
		while not choiceValid:
			choice = str(input("Which door do you want to try?"))
			if choice == "left" or choice == "LEFT" or choice == "Left":
				choiceValid = True
				leftChoice5()
				nextRoom = True
			elif choice == "right" or choice == "RIGHT" or choice == "Right":
				choiceValid = True
				rightChoice5()
				nextRoom = True
			else:
                            print "That is not an exit.  Please try again."

rooms = [room1, room2, room3, room4, room5]
def main():
    intro()
    room0()
    for i in range(3):
        rooms[randint(0, (len(rooms))-1)]()
    gameover()
        
main()
