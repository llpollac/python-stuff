#Lara Pollack
from random import * #We need the random library to shuffle the deck

global northSpades
global northHearts
global northDiamonds
global northClubs
   
global eastSpades
global eastHearts
global eastDiamonds 
global eastClubs

global southSpades
global southHearts
global southDiamonds
global southClubs

global westSpades
global westHearts
global westDiamonds
global westClubs

spades = "spades" #attempting to make this as robust against user input error as possible
hearts = "hearts"
diamonds = "diamonds"
clubs = "clubs" 
#a card object is a 2-tuple.  The element of the tuple are face value and suit. 14 = A, 13 = K, 12 = Q, 11 = J
#declared as variables to make it easier for me to work with them 
#spades:
SA = (14, "spades")
SK = (13, "spades")
SQ = (12, "spades")
SJ = (11, "spades")
S10 = (10, "spades")
S9 = (9, "spades")
S8 = (8, "spades")
S7 = (7, "spades")
S6 = (6, "spades")
S5 = (5, "spades")
S4 = (4, "spades")
S3 = (3, "spades")
S2 = (2, "spades")
#hearts:
HA = (14, "hearts")
HK = (13, "hearts")
HQ = (12, "hearts")
HJ = (11, "hearts")
H10 = (10, "hearts")
H9 = (9, "hearts")
H8 = (8, "hearts")
H7 = (7, "hearts")
H6 = (6, "hearts")
H5 = (5, "hearts")
H4 = (4, "hearts")
H3 = (3, "hearts")
H2 = (2, "hearts")
#diamonds:
DA = (14, "diamonds")
DK = (13, "diamonds")
DQ = (12, "diamonds")
DJ = (11, "diamonds")
D10 = (10, "diamonds")
D9 = (9, "diamonds")
D8 = (8, "diamonds")
D7 = (7, "diamonds")
D6 = (6, "diamonds")
D5 = (5, "diamonds")
D4 = (4, "diamonds")
D3 = (3, "diamonds")
D2 = (2, "diamonds")
#clubs:
CA = (14, "clubs")
CK = (13, "clubs")
CQ = (12, "clubs")
CJ = (11, "clubs")
C10 = (10, "clubs")
C9 = (9, "clubs")
C8 = (8, "clubs")
C7 = (7, "clubs")
C6 = (6, "clubs")
C5 = (5, "clubs")
C4 = (4, "clubs")
C3 = (3, "clubs")
C2 = (2, "clubs")
#unshuffledDeck is a list that contains all the cards in a standard 52 card deck (in order to make sure I didn't forget any)
unshuffledDeck = [SA, SK, SQ, SJ, S10, S9, S8, S7, S6, S5, S4, S3, S2, HA, HK, HQ, HJ, H10, H9, H8, H7, H6, H5, H4, H3, H2, DA, DK, DQ, DJ, D10, D9, D8, D7, D6, D5, D4, D3, D2, CA, CK, CQ, CJ, C10, C9, C8, C7, C6, C5, C4, C3, C2]

def nonzeromin(List): #returns the lowest non-zero value in a list
    nonzerolist=[]
    for i in List: #for every item in the list
        if i != 0: #if the item isn't zero
            nonzerolist.append(i) #put it in the list of nonzero values
    if len(nonzerolist)==0: #if either all values in List are zero or zero is an empty list
        return "Empty List" #it has to return something not an error value, and a string doesn't conflict with how I use the function later
    else:
        return min(nonzerolist) #return lowest value in list of non-zero values

def shuffleDeck(): #shuffles the deck (puts the cards into a random order
    shuffledDeck = []
    unshuffledDeckCopy = unshuffledDeck[:] #make a copy of the unshuffled deck (so the original unshuffled deck remains stable
    while len(unshuffledDeckCopy) > 0: #while still cards in the deck to be shuffled
        length = len(unshuffledDeckCopy)-1
        card = unshuffledDeckCopy.pop(randint(0, length)) #take a random card from the deck
        shuffledDeck.append(card) #and put it into the shuffled deck
    return shuffledDeck #return the shuffled deck

def deal(): #deals thirteen cards to each of four players, organized according to suit and rank
    northSpades = [] #north's hand, in four suits
    northHearts = []
    northDiamonds = []
    northClubs = []
    
    eastSpades = [] #east's hand, in four suits
    eastHearts = []
    eastDiamonds = []
    eastClubs = []

    southSpades = [] #south's hand, in four suits
    southHearts = []
    southDiamonds = []
    southClubs = []

    westSpades = [] #west's hand, in four suits
    westHearts = []
    westDiamonds = []
    westClubs = []

    deck = shuffleDeck() #dealing from a shuffled deck

    while len(deck) > 0: #while there are cards to deal out
        north = deck.pop() #take a card from the deck
        if north[1] == "spades":#and put it in the relevent part of the hand according to suit
            northSpades.append(north)
        elif north[1] == "hearts":
            northHearts.append(north)
        elif north[1] == "diamonds":
            northDiamonds.append(north)
        elif north[1] == "clubs":
            northClubs.append(north)

        east = deck.pop()#repeat for each of the other players
        if east[1] == "spades":
            eastSpades.append(east)
        elif east[1] == "hearts":
            eastHearts.append(east)
        elif east[1] == "diamonds":
            eastDiamonds.append(east)
        elif east[1] == "clubs":
            eastClubs.append(east)

        south = deck.pop()
        if south[1] == "spades":
            southSpades.append(south)
        elif south[1] == "hearts":
            southHearts.append(south)
        elif south[1] == "diamonds":
            southDiamonds.append(south)
        elif south[1] == "clubs":
            southClubs.append(south)

        west = deck.pop()
        if west[1] == "spades":
            westSpades.append(west)
        elif west[1] == "hearts":
            westHearts.append(west)
        elif west[1] == "diamonds":
            westDiamonds.append(west)
        elif west[1] == "clubs":
            westClubs.append(west)

    northSpades.sort(reverse = True) #sort all the parts of the hands in descending order (A high, 2 low)
    northHearts.sort(reverse = True)
    northDiamonds.sort(reverse = True)
    northClubs.sort(reverse = True)

    eastSpades.sort(reverse = True)
    eastHearts.sort(reverse = True)
    eastDiamonds.sort(reverse = True)
    eastClubs.sort(reverse = True)

    southSpades.sort(reverse = True)
    southHearts.sort(reverse = True)
    southDiamonds.sort(reverse = True)
    southClubs.sort(reverse = True)

    westSpades.sort(reverse = True)
    westHearts.sort(reverse = True)
    westDiamonds.sort(reverse = True)
    westClubs.sort(reverse = True)

    northHand = [northSpades, northHearts, northDiamonds, northClubs]#put the different parts of the hand together
    eastHand = [eastSpades, eastHearts, eastDiamonds, eastClubs]
    southHand = [southSpades, southHearts, southDiamonds, southClubs]
    westHand = [westSpades, westHearts, westDiamonds, westClubs]

    return northHand, eastHand, southHand, westHand #and return the hand
global handCount
handCount = 0 #counter for how many hands have been played
global leader
global trumps
trumps="dummy"

def trick(leader): #play a single trick
    global northCard
    global eastCard
    global southCard
    global westCard
    global winner
    winner = "dummy"
    ledCard = "dummy"
    if leader == "north": #north leads
        
        #north plays a card
        if trumps == "spades": #if trumps is spades
            if len(northHearts) == nonzeromin([len(northHearts), len(northDiamonds), len(northClubs)]): #play the highest card in shortest non-trump suit
                ledCard = northHearts.pop(0)
            elif len(northDiamonds)== nonzeromin([len(northHearts), len(northDiamonds), len(northClubs)]):
                ledCard = northDiamonds.pop(0)
            elif len(northClubs) == nonzeromin([len(northHearts), len(northDiamonds), len(northClubs)]):
                ledCard = northClubs.pop(0)
            else:
                ledCard = northSpades.pop(0) #unless all you have left are trumps, in which case play the highest trump
        elif trumps == "hearts":
            if len(northSpades) == nonzeromin([len(northSpades), len(northDiamonds), len(northClubs)]):
                ledCard = northSpades.pop(0)
            elif len(northDiamonds) == nonzeromin([len(northSpades), len(northDiamonds), len(northClubs)]):
                ledCard = northDiamonds.pop(0)
            elif len(northClubs) == nonzeromin([len(northSpades), len(northDiamonds), len(northClubs)]):
                ledCard = northClubs.pop(0)
            else:
                ledCard = northHearts.pop(0)
        elif trumps == "diamonds":
            if len(northSpades)== nonzeromin([len(northSpades), len(northHearts), len(northClubs)]):
                ledCard = northSpades.pop(0)
            elif len(northHearts) == nonzeromin([len(northSpades), len(northHearts), len(northClubs)]):
                ledCard = northHearts.pop(0)
            elif len(northClubs) == nonzeromin([len(northSpades), len(northHearts), len(northClubs)]):
                ledCard = northClubs.pop(0)
            else:
                ledCard = northDiamonds.pop(0)
        else:
            if len(northSpades) == nonzeromin([len(northSpades), len(northHearts), len(northDiamonds)]):
                ledCard = northSpades.pop(0)
            elif len(northHearts) == nonzeromin([len(northSpades), len(northHearts), len(northDiamonds)]):
                ledCard = northHearts.pop(0)
            elif len(northDiamonds) == nonzeromin([len(northSpades), len(northHearts), len(northDiamonds)]):
                ledCard = northDiamonds.pop(0)
            else:
                ledCard = northClubs.pop(0)
       
        suit = ledCard[1] #the suit for the trick is the suit of the led card
        print "North: ", ledCard #print the card that's played
        northCard = ledCard #and the card north leads is north's card

        #east plays a card
        if suit == "spades" and len(eastSpades)>0:#first, follow suit.  If you have a card in that suit, play the highest in that suit
            eastCard = eastSpades.pop(0)
        elif suit == "hearts" and len(eastHearts) >0:
            eastCard = eastHearts.pop(0)
        elif suit == "diamonds" and len(eastDiamonds)>0:
            eastCard = eastDiamonds.pop(0)
        elif suit == "clubs" and len(eastClubs)>0:
            eastCard = eastClubs.pop(0)
        elif trumps == "spades" and len(eastSpades)>0: #void in led suit, so start trumping.  Play highest trump in hand
            eastCard = eastSpades.pop(0)
        elif trumps == "hearts" and len(eastHearts)>0:
            eastCard = eastHearts.pop(0)
        elif trumps == "diamonds" and len(eastDiamonds)>0:
            eastCard = eastDiamonds.pop(0)
        elif trumps == "clubs" and len(eastClubs)>0:
            eastCard = eastClubs.pop(0)
        elif len(eastSpades) == nonzeromin([len(eastSpades), len(eastHearts), len(eastDiamonds), len(eastClubs)]): #and if you don't have any trumps, play lowest card in shortest suit
            eastCard = eastSpades.pop()
        elif len(eastHearts) == nonzeromin([len(eastSpades), len(eastHearts), len(eastDiamonds), len(eastClubs)]):
            eastCard = eastHearts.pop()
        elif len(eastDiamonds) == nonzeromin([len(eastSpades), len(eastHearts), len(eastDiamonds), len(eastClubs)]):
            eastCard = eastDiamonds.pop()
        else:
            eastCard = eastClubs.pop()
        print "East: ", eastCard

        #south (human) plays a card
        southCard = input("Which card will you play?") #human player (note: there's no safeguard built in to make sure this is a valid card to play; rather, it trusts the human player to have the judgement to play a card in its hand and to follow the rules of what card can be played.
        print "South: ", southCard #print what card south played
        if southCard in southSpades: #and take it out of your hand
            southSpades.remove(southCard)
        elif southCard in southHearts:
            southHearts.remove(southCard)
        elif southCard in southDiamonds:
            southDiamonds.remove(southCard)
        else:
            southClubs.remove(southCard)

        #west plays a card
        if suit == "spades" and len(westSpades)>0:#follows same proceedure for playing a card as east does (all non-leading computer players do this)
            westCard = westSpades.pop(0)
        elif suit == "hearts" and len(westHearts)>0:
            westCard = westHearts.pop(0)
        elif suit == "diamonds" and len(westDiamonds)>0:
            westCard = westDiamonds.pop(0)
        elif suit == "clubs" and len(westClubs)>0:
            westCard = westClubs.pop(0)
        elif trumps == "spades" and len(westSpades)>0:
            westCard = westSpades.pop(0)
        elif trumps == "hearts" and len(westHearts):
            westCard = westHearts.pop(0)
        elif trumps == "diamonds" and len(westDiamonds)>0: 
            westCard = westDiamonds.pop(0)
        elif trumps == "clubs" and len(westClubs)>0:
            westCard = westClubs.pop(0)
        elif len(westSpades) == nonzeromin([len(westSpades), len(westHearts), len(westDiamonds), len(westClubs)]):
            westCard = westSpades.pop()
        elif len(westHearts) == nonzeromin([len(westSpades), len(westHearts), len(westDiamonds), len(westClubs)]):
            westCard = westHearts.pop()
        elif len(westDiamonds) == nonzeromin([len(westSpades), len(westHearts), len(westDiamonds), len(westClubs)]):
            westCard = westDiamonds.pop()
        else:
            westCard = westClubs.pop()

        print "West: ", westCard

    elif leader == "east": #and the above is the general scheme of how a trick works, but here follow cases for different leaders
        #east plays a card
        if trumps == "spades":
            if len(eastHearts) == nonzeromin([len(eastHearts), len(eastDiamonds), len(eastClubs)]):#play the highest card in shortest non-trump suit
                ledCard = eastHearts.pop(0)
            elif len(eastDiamonds)== nonzeromin([len(eastHearts), len(eastDiamonds), len(eastClubs)]):
                ledCard = eastDiamonds.pop(0)
            elif len(eastClubs) == nonzeromin([len(eastHearts), len(eastDiamonds), len(eastClubs)]):
                ledCard = eastClubs.pop(0)
            else:
                ledCard = eastSpades.pop(0)
        elif trumps == "hearts":
            if len(eastSpades) == nonzeromin([len(eastSpades), len(eastDiamonds), len(eastClubs)]):
                ledCard = eastSpades.pop(0)
            elif len(eastDiamonds) == nonzeromin([len(eastSpades), len(eastDiamonds), len(eastClubs)]):
                ledCard = eastDiamonds.pop(0)
            elif len(eastClubs) == nonzeromin([len(eastSpades), len(eastDiamonds), len(eastClubs)]):
                ledCard = eastClubs.pop(0)
            else:
                ledCard = eastHearts.pop(0)
        elif trumps == "diamonds":
            if len(eastSpades)== nonzeromin([len(eastSpades), len(eastHearts), len(eastClubs)]):
                ledCard = eastSpades.pop(0)
            elif len(eastHearts) == nonzeromin([len(eastSpades), len(eastHearts), len(eastClubs)]):
                ledCard = eastHearts.pop(0)
            elif len(eastClubs) == nonzeromin([len(eastSpades), len(eastHearts), len(eastClubs)]):
                ledCard = eastClubs.pop(0)
            else:
                ledCard = eastDiamonds.pop(0)
        else:
            if len(eastSpades) == nonzeromin([len(eastSpades), len(eastHearts), len(eastDiamonds)]):
                ledCard = eastSpades.pop(0)
            elif len(eastHearts) == nonzeromin([len(eastSpades), len(eastHearts), len(eastDiamonds)]):
                ledCard = eastHearts.pop(0)
            elif len(eastDiamonds) == nonzeromin([len(eastSpades), len(eastHearts), len(eastDiamonds)]):
                ledCard = eastDiamonds.pop(0)
            else:
                ledCard = eastClubs.pop(0)
        suit = ledCard[1]
        print "East: ", ledCard
        eastCard = ledCard

        #south (human) plays a card
        southCard = input("Which card will you play?") #human player
        print "South: ", southCard
        if southCard in southSpades:
            southSpades.remove(southCard)
        elif southCard in southHearts:
            southHearts.remove(southCard)
        elif southCard in southDiamonds:
            southDiamonds.remove(southCard)
        else:
            southClubs.remove(southCard)

        #west plays a card
        if suit == "spades" and len(westSpades)>0:#length of suit for west > 0:
            westCard = westSpades.pop(0)
        elif suit == "hearts" and len(westHearts)>0:
            westCard = westHearts.pop(0)
        elif suit == "diamonds" and len (westDiamonds)>0:
            westCard = westDiamonds.pop(0)
        elif suit == "clubs" and len(westClubs)>0:
            westCard = westClubs.pop(0)
        elif trumps == "spades" and len(westSpades)>0:
            westCard = westSpades.pop(0)
        elif trumps == "hearts" and len(westHearts)>0:
            westCard = westHearts.pop(0)
        elif trumps == "diamonds" and len(westHearts)>0:
            westCard = westDiamonds.pop(0)
        elif trumps == "clubs" and len(westClubs)>0:
            westCard = westClubs.pop(0)
        elif len(westSpades) == nonzeromin([len(westSpades), len(westHearts), len(westDiamonds), len(westClubs)]):
            westCard = westSpades.pop()
        elif len(westHearts) == nonzeromin([len(westSpades), len(westHearts), len(westDiamonds), len(westClubs)]):
            westCard = westHearts.pop()
        elif len(westDiamonds) == nonzeromin([len(westSpades), len(westHearts), len(westDiamonds), len(westClubs)]):
            westCard = westDiamonds.pop()
        else:
            westCard = westClubs.pop()

        print "West: ", westCard

        #north plays a card
        if suit == "spades" and len(northSpades)>0:
            northCard = northSpades.pop(0)
        elif suit == "hearts" and len(northHearts)>0:
            northCard = northHearts.pop(0)
        elif suit == "diamonds" and len(northDiamonds)>0:
            northCard = northDiamonds.pop(0)
        elif suit == "clubs" and len(northClubs)>0:
            northCard = northClubs.pop(0)
        elif trumps == "spades" and len(northSpades)>0:
            northCard = northSpades.pop(0)
        elif trumps == "hearts" and len(northHearts)>0:
            northCard = northHearts.pop(0)
        elif trumps == "diamonds" and len(northDiamonds)>0:
            northCard = northDiamonds.pop(0)
        elif trumps == "clubs" and len(northClubs)>0:
            northCard = northClubs.pop(0)
        elif len(northSpades) == nonzeromin([len(northSpades), len(northHearts), len(northDiamonds), len(northClubs)]):
            northCard = northSpades.pop()
        elif len(northHearts) == nonzeromin([len(northSpades), len(northHearts), len(northDiamonds), len(northClubs)]):
            northCard = northHearts.pop()
        elif len(northDiamonds) == nonzeromin([len(northSpades), len(northHearts), len(northDiamonds), len(northClubs)]):
            northCard = northDiamonds.pop()
        else:
            northCard = northClubs.pop()

        print "North: ", northCard

    elif leader == "south":
        #south (human) plays a card
        ledCard = input("Which card will you play? ")
        suit = ledCard[1]
        print "South: ", ledCard
        if ledCard[1] == "spades":
            southSpades.remove(ledCard)
        elif ledCard[1] == "hearts":
            southHearts.remove(ledCard)
        elif ledCard[1] == "diamonds":
            southDiamonds.remove(ledCard)
        else:
            southClubs.remove(ledCard)
        southCard = ledCard

        #west plays a card
        if suit == "spades" and len(westSpades)>0:
            westCard = westSpades.pop(0)
        elif suit == "hearts" and len(westHearts):
            westCard = westHearts.pop(0)
        elif suit == "diamonds" and len(westDiamonds)>0:
            westCard = westDiamonds.pop(0)
        elif suit == "clubs" and len(westClubs)>0:
            westCard = westClubs.pop(0)
        elif trumps == "spades" and len(westSpades)>0:
            westCard = westSpades.pop(0)
        elif trumps == "hearts" and len(westHearts)>0:
            westCard = westHearts.pop(0)
        elif trumps == "diamonds" and len(westDiamonds)>0:
            westCard = westDiamonds.pop(0)
        elif trumps == "clubs" and len(westClubs)>0:
            westCard = westClubs.pop(0)
        elif len(westSpades) == nonzeromin([len(westSpades), len(westHearts), len(westDiamonds), len(westClubs)]):
            westCard = westSpades.pop()
        elif len(westHearts) == nonzeromin([len(westSpades), len(westHearts), len(westDiamonds), len(westClubs)]):
            westCard = westHearts.pop()
        elif len(westDiamonds) == nonzeromin([len(westSpades), len(westHearts), len(westDiamonds), len(westClubs)]):
            westCard = westDiamonds.pop()
        else:
            westCard = westClubs.pop()

        print "West: ", westCard

        #north plays a card
        if suit == "spades":
            if len(northSpades)>0:
                northCard = northSpades.pop(0)
        elif suit == "hearts":
            if len(northHearts)>0:
                northCard = northHearts.pop(0)
        elif suit == "diamonds":
            if len(northDiamonds)>0:
                northCard = northDiamonds.pop(0)
        elif suit == "clubs":
            if len(northClubs)>0:
                northCard = northClubs.pop(0)
        elif trumps == "spades":
            if len(northSpades)>0:
                northCard = northSpades.pop(0)
        elif trumps == "hearts":
            if len(northHearts)>0:
                northCard = northHearts.pop(0)
        elif trumps == "diamonds":
            if len(northDiamonds)>0:
                northCard = northDiamonds.pop(0)
        elif trumps == "clubs":
            if len(northClubs)>0:
                northCard = northClubs.pop(0)
        elif len(northSpades) == nonzeromin([len(northSpades), len(northHearts), len(northDiamonds), len(northClubs)]):
            northCard = northSpades.pop()
        elif len(northHearts) == nonzeromin([len(northSpades), len(northHearts), len(northDiamonds), len(northClubs)]):
            northCard = northHearts.pop()
        elif len(northDiamonds) == nonzeromin([len(northSpades), len(northHearts), len(northDiamonds), len(northClubs)]):
            northCard = northDiamonds.pop()
        else:
            northCard = northClubs.pop()

        print "North: ", northCard

        #east plays a card
        if suit == "spades" and len(eastSpades)>0:
            eastCard = eastSpades.pop(0)
        elif suit == "hearts" and len(eastHearts)>0:
            eastCard = eastHearts.pop(0)
        elif suit == "diamonds" and len(eastDiamonds)>0:
            eastCard = eastDiamonds.pop(0)
        elif suit == "clubs" and len(eastClubs)>0:
            eastCard = eastClubs.pop(0)
        elif trumps == "spades" and len(eastSpades)>0:
            eastCard = eastSpades.pop(0)
        elif trumps == "hearts" and len(eastHearts)>0:
            eastCard = eastHearts.pop(0)
        elif trumps == "diamonds" and len(eastDiamonds)>0:
            eastCard = eastDiamonds.pop(0)
        elif trumps == "clubs" and len(eastClubs)>0:
            eastCard = eastClubs.pop(0)
        elif len(eastSpades) == nonzeromin([len(eastSpades), len(eastHearts), len(eastDiamonds), len(eastClubs)]):
            eastCard = eastSpades.pop()
        elif len(eastHearts) == nonzeromin([len(eastSpades), len(eastHearts), len(eastDiamonds), len(eastClubs)]):
            eastCard = eastHearts.pop()
        elif len(eastDiamonds) == nonzeromin([len(eastSpades), len(eastHearts), len(eastDiamonds), len(eastClubs)]):
            eastCard = eastDiamonds.pop()
        else:
            eastCard = eastClubs.pop()

        print "East: ", eastCard

    elif leader == "west":
        #west plays a card
        if trumps == "spades":
            if len(westHearts) == nonzeromin([len(westHearts), len(westDiamonds), len(westClubs)]):
                ledCard = westHearts.pop(0)
            elif len(westDiamonds)== nonzeromin([len(westHearts), len(westDiamonds), len(westClubs)]):
                ledCard = westDiamonds.pop(0)
            elif len(westClubs) == nonzeromin([len(westHearts), len(westDiamonds), len(westClubs)]):
                ledCard = westClubs.pop(0)
            else:
                ledCard = westSpades.pop(0)
        elif trumps == "hearts":
            if len(westSpades) == nonzeromin([len(westSpades), len(westDiamonds), len(westClubs)]):
                ledCard = westSpades.pop(0)
            elif len(westDiamonds) == nonzeromin([len(westSpades), len(westDiamonds), len(westClubs)]):
                ledCard = westDiamonds.pop(0)
            elif len(westClubs) == nonzeromin([len(westSpades), len(westDiamonds), len(westClubs)]):
                ledCard = westClubs.pop(0)
            else:
                ledCard = westHearts.pop(0)
        elif trumps == "diamonds":
            if len(westSpades)== nonzeromin([len(westSpades), len(westHearts), len(westClubs)]):
                ledCard = westSpades.pop(0)
            elif len(westHearts) == nonzeromin([len(westSpades), len(westHearts), len(westClubs)]):
                ledCard = westHearts.pop(0)
            elif len(westClubs) == nonzeromin([len(westSpades), len(westHearts), len(westClubs)]):
                ledCard = westClubs.pop(0)
            else:
                ledCard = westDiamonds.pop(0)
        else:
            if len(westSpades) == nonzeromin([len(westSpades), len(westHearts), len(westDiamonds)]):
                ledCard = westSpades.pop(0)
            elif len(westHearts) == nonzeromin([len(westSpades), len(westHearts), len(westDiamonds)]):
                ledCard = westHearts.pop(0)
            elif len(westDiamonds) == nonzeromin([len(westSpades), len(westHearts), len(westDiamonds)]):
                ledCard = westDiamonds.pop(0)
            else:
                ledCard = westClubs.pop(0)
        
        suit = ledCard[1]
        print "West: ", ledCard
        westCard = ledCard

        #north plays a card
        if suit == "spades" and len(northSpades)>0:
            northCard = northSpades.pop(0)
        elif suit == "hearts" and len(northHearts)>0:
            northCard = northHearts.pop(0)
        elif suit == "diamonds" and len(northDiamonds)>0:
            northCard = northDiamonds.pop(0)
        elif suit == "clubs" and len(northClubs)>0:
            northCard = northClubs.pop(0)
        elif trumps == "spades" and len(northSpades)>0:
            northCard = northSpades.pop(0)
        elif trumps == "hearts" and len(northHearts)>0:
            northCard = northHearts.pop(0)
        elif trumps == "diamonds" and len(northDiamonds)>0:
            northCard = northDiamonds.pop(0)
        elif trumps == "clubs" and len(northClubs)>0:
            northCard = northClubs.pop(0)
        elif len(northSpades) == nonzeromin([len(northSpades), len(northHearts), len(northDiamonds), len(northClubs)]):
            northCard = northSpades.pop()
        elif len(northHearts) == nonzeromin([len(northSpades), len(northHearts), len(northDiamonds), len(northClubs)]):
            northCard = northHearts.pop()
        elif len(northDiamonds) == nonzeromin([len(northSpades), len(northHearts), len(northDiamonds), len(northClubs)]):
            northCard = northDiamonds.pop()
        else:
            northCard = northClubs.pop()

        print "North: ", northCard

        #east plays a card
        if suit == "spades" and len(eastSpades)>0:
            eastCard = eastSpades.pop(0)
        elif suit == "hearts" and len(eastHearts)>0:
            eastCard = eastHearts.pop(0)
        elif suit == "diamonds" and len(eastDiamonds)>0:
            eastCard = eastDiamonds.pop(0)
        elif suit == "clubs" and len(eastClubs)>0:
            eastCard = eastClubs.pop(0)
        elif trumps == "spades" and len(eastSpades)>0:
            eastCard = eastSpades.pop(0)
        elif trumps == "hearts" and len(eastHearts)>0:
            eastCard = eastHearts.pop(0)
        elif trumps == "diamonds" and len(eastDiamonds)>0:
            eastCard = eastDiamonds.pop(0)
        elif trumps == "clubs" and len(eastClubs)>0:
            eastCard = eastClubs.pop(0)
        elif len(eastSpades) == nonzeromin([len(eastSpades), len(eastHearts), len(eastDiamonds), len(eastClubs)]):
            eastCard = eastSpades.pop()
        elif len(eastHearts) == nonzeromin([len(eastSpades), len(eastHearts), len(eastDiamonds), len(eastClubs)]):
            eastCard = eastHearts.pop()
        elif len(eastDiamonds) == nonzeromin([len(eastSpades), len(eastHearts), len(eastDiamonds), len(eastClubs)]):
            eastCard = eastDiamonds.pop()
        else:
            eastCard = eastClubs.pop()

        print "East: ", eastCard

        #south (human) plays a card
        southCard = input("Which card will you play?") #human player
        print "South: ", southCard
        if southCard in southSpades:
            southSpades.remove(southCard)
        elif southCard in southHearts:
            southHearts.remove(southCard)
        elif southCard in southDiamonds:
            southDiamonds.remove(southCard)
        else:
            southClubs.remove(southCard)
                              
    playedCards = [northCard, eastCard, southCard, westCard] #the cards that have been played this trick
    trumpCards = [] #will hold any trump cards
    compareCards = [] #will hold any suit cards
    for i in playedCards: #for every card played this trick
        if i[1] == trumps:#if it's a trump card
            trumpCards.append(i)#put it with the trump cards
        elif i[1] == suit:#if it follows suit
            compareCards.append(i)#put it with the cards in that suit
    trumpCards.sort(reverse=True)#sort highest first
    compareCards.sort(reverse=True)#ditto
    if len(trumpCards)>0: #if a trump card has been played
        winner = trumpCards.pop(0)#winner is the highest trump card
    else:#otherwise
        winner = compareCards.pop(0)#winner is the highest card in suit
    return winner
def playHand(): #plays one hand of whist
    hand = deal()#deal cards
    northHand = hand[0]#the hands of the players
    eastHand = hand[1]
    southHand = hand[2]
    westHand = hand[3]

    global northSpades
    global northHearts
    global northDiamonds
    global northClubs
    global eastSpades
    global eastHearts
    global eastDiamonds
    global eastClubs
    global southSpades
    global southHearts
    global southDiamonds
    global southClubs
    global westSpades
    global westHearts
    global westDiamonds
    global westClubs
    
    
    northSpades = northHand[0]
    northHearts = northHand[1]
    northDiamonds = northHand[2]
    northClubs = northHand[3]
    
    eastSpades = eastHand[0]
    eastHearts = eastHand[1]
    eastDiamonds = eastHand[2]
    eastClubs = eastHand[3]

    southSpades = southHand[0]
    southHearts = southHand[1]
    southDiamonds = southHand[2]
    southClubs = southHand[3]

    westSpades = westHand[0]
    westHearts = westHand[1]
    westDiamonds = westHand[2]
    westClubs = westHand[3]

    global trumps
    trumpCount = handCount % 4 #trumps cycles handwise in bridge order
    if trumpCount == 0:
        trumps = "spades"
    elif trumpCount == 1:
        trumps = "hearts"
    elif trumpCount == 2:
        trumps = "diamonds"
    elif trumpCount == 3:
        trumps = "clubs"

    leaderCount = handCount % 4 #leader for 1st trick
    if leaderCount == 0:
        leader = "north"
    elif leaderCount == 1:
        leader = "east"
    elif leaderCount == 2:
        leader = "south"
    elif leaderCount == 3:
        leader = "west"

    NorthSouthTricks = 0 #counter for how many tricks north/south partnership has taken
    EastWestTricks = 0#counter for how many tricks east/west partnership has taken

    print "Trumps is ", trumps #declaration of trumps for hand
    for i in range(13):#thirteen tricks in a hand (at the end of the hand, players' hands will be empty [all cards will be played])
        print "~~~~~" #visual dividing for the benefit of the human
        print "start of trick"
        print southHand[0]+southHand[1]+southHand[2]+southHand[3] #what cards are currently in the human's hand
        winner = trick(leader) #play the trick, who wins the trick?

        if winner == northCard: #north wins the trick
            NorthSouthTricks += 1#plus 1 to the partnership's counter
            leader = "north" #north leads the next trick
            print "north takes the trick" #for the human's benefit, to see who took the trick
        elif winner == eastCard: #ditto for east
            EastWestTricks +=1
            leader = "east"
            print "east takes the trick"
        elif winner == southCard: #ditto for south
            NorthSouthTricks +=1
            leader = "south"
            print "south takes the trick"
        elif winner == westCard:#ditto for west
            EastWestTricks +=1
            leader = "west"
            print "west takes the trick"
        
        #leader leads a card
        #play goes clockwise: NESW, ESWN, SWNE, WNES
        #spades are Hand[0], hearts are Hand[1], diamonds are Hand[2], clubs are Hand[3]
        #card led[1] becomes suit
        #play highest card in suit
        #if void in suit, play highest trump
        #if void in trump, play lowest in shortest other suit

        #highest trump wins trick
        #if no trump played, highest card in suit wins trick
        #+1 to partnership score for winner of trick

        #winner of trick becomes leader

#human player is south, partnered with north

    return NorthSouthTricks, EastWestTricks #at the end of the hand, how many tricks did each partnership take?

def main(): #play a full game of whist
    NorthSouthScore = 0 #counter for north/south score
    EastWestScore = 0 #counter for east/west score
    print "We are now going to play whist." #instructions for game
    print "You are South.  Type a card exactly as it appears to play it." #please don't break the program, human player!
    print "14 = Ace, 13 = King, 12 = Queen, 11 = Jack" #since we're dealing with numeric rank rather than printing the face cards (and ace is high)
    while (NorthSouthScore < 5 and EastWestScore <5): #while neither partnership has scored 5
        print "~~~~~~~~~" #visual divider
        print "Start of new hand."
        score = playHand() #play the hand
        if score[0] > score[1]: #if north/south has taken more tricks than east/west
            NorthSouthScore += (score[0]-6) #add the value of the tricks minus six to their score
        else:
            EastWestScore += (score[1]-6) #ditto, except for east/west
        print "Hand score: North/South: ", score[0], "East/West: ", score[1] #how many tricks everyone took
        print "Score: North/South: ", NorthSouthScore, ", East/West: ", EastWestScore#how the game score is doing
        global handCount
        handCount+=1 #plus 1 to the hand count
    if NorthSouthScore > 5 and EastWestScore != NorthSouthScore: #north/south broke 5 and the game's not tied
        print "Yay, you won!"
    elif EastWestScore > 5 and NorthSouthScore != EastWestScore: #east/west broke 5 and the game's not tied
        print "Sorry, East/West won."
    else:
        print "Yay, you tied!" #they tied
    print "Thank you for playing." #be polite

main()
