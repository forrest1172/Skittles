#bullshit/skittles remake 
#♥♦♣♠
import random
class Card:

    def __init__(self,cardNum,suit,color):
        self.cardNum = cardNum
        self.suit = suit
        self.color = color
    def __repr__(self):
        return "This is a {color} {cardNum} of {suit}".format(color=self.color,cardNum=self.cardNum, suit=self.suit)

def MakeCards():
    currentNum = 1
    while currentNum <= 13:
        #hearts
        if(currentNum == 11):
           allCards.append(Card("Jack","Hearts","Red"))
           allCards.append(Card("Jack","Diamonds","Red"))
           allCards.append(Card("Jack","Spades","Black"))
           allCards.append(Card("Jack","Clubs","Black"))
        elif(currentNum == 12):
           allCards.append(Card("Queen","Hearts","Red"))
           allCards.append(Card("Queen","Diamonds","Red"))
           allCards.append(Card("Queen","Spades","Black"))
           allCards.append(Card("Queen","Clubs","Black"))
        elif(currentNum == 13):
           allCards.append(Card("King","Hearts","Red"))
           allCards.append(Card("King","Diamonds","Red"))
           allCards.append(Card("King","Spades","Black"))
           allCards.append(Card("King","Clubs","Black"))
        else:
           allCards.append(Card(currentNum,"Hearts","Red"))
           allCards.append(Card(currentNum,"Diamonds","Red"))
           allCards.append(Card(currentNum,"Spades","Black"))
           allCards.append(Card(currentNum,"Clubs","Black"))
        currentNum += 1
    #print(list(allCards))
allCards = []

def DealCards():
    pass

def WaitForInput():
    playerIn = input(" ")
    if(playerIn == "cards") or (playerIn == "count"):
        print(list(playerList))
    else:
        print("Incorrect input")
        return

class Player:
    def __init__(self,name,numOfCards,isNPC):
        self.name = name
        self.numOfCards = numOfCards
        self.isNPC = False
    def __repr__(self):
        return "Player {name} has {numofcards} cards".format(numofcards = self.numOfCards, name = self.name)
block = """
|||||__SKITTLES__|||||
        |_____|
        |     |
"""
print(block)
playerStart = input("Welcome to the skittles table. Please press 'ENTER' to continue \n")

numOfPlayers = random.randint(4,10)
MakeCards()
playerList = []
num = 1
for newPlayer in range(0,numOfPlayers):
    name = str(num)
    playerList.append(Player(name,0,True))
    num += 1
playerName = input("Please enter your name. \n")

print("Welcome " + str(playerName) + " You will be playing with " + (str(numOfPlayers)) + " other players")

DealCards()

WaitForInput()
