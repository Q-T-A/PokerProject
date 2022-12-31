import random as rand
import pokerMethod

def shuffle(deck):
    check = 0
    #arr = [i + 1 for i in range(0,52)]
    while check < 52:
        r = rand.sample(range(0,52), 2)
        storage = deck[r[0]] 
        deck[r[0]] = deck[r[1]]
        deck[r[1]] = storage
        check = check + 1

def bubbleSort(deck):
    deck1 = deck.copy()
    for a in range (0,5):
        while deck1[a] > 13:
            deck1[a] = deck1[a] - 13 #this negates suits so we are only 
            #looking at faces because implementation represents the entire 
            #deck as integers from 1 to 52 you must subract 13 continuously
            #so the cards are sorted based on face values
    for i in range(0,4):
        for j in range(0, 4 - i):
            if deck1[j] > deck1[j + 1]:
                storage1 = deck1[j]
                deck1[j] = deck1[j + 1]
                deck1[j + 1] = storage1
                storage = deck[j]
                deck[j] = deck[j + 1]
                deck[j + 1] = storage
                #I must sort both the copy and the original because the copy
                #is what is being referenced for the sorting algo
                #I can not return the copy because the suit data has been
                #lost during the conversion from suit to solely face values

def play(deck):
    player1 = [0,0,0,0,0]
    player2 = [0,0,0,0,0]
    cardsDealt = 0
    for i in range (0,5):
        player1[i] = deck.pop(0) #give player top card
        player2[i] = deck.pop(0)
        cardsDealt = cardsDealt + 2 #two cards have been dealt each time
    bubbleSort(player1)
    bubbleSort(player2)
    print(f"Player 1's hand: {handToString(player1)}")
    print(f"Player 2's hand: {handToString(player2)}")
    decision(player1,player2,deck)
    
def decision(player1,player2,deck):
    print("\nPlayer 1 type Y to keep your card and N to receive a new card")
    i = 0
    while i < 5:
        x = input(f'would you like to keep {handToString(player1[i])} (Y/N) ')
        if x.lower() == 'n':
            deck.append(player1[i]) #put old card back in deck
            player1[i] = deck.pop(0) #dish out new card
            i = i + 1
        elif x.lower() == 'y':
            i = i + 1
        else:
            print("Please enter either Y or N")
            
    i = 0 #reset i value
    print("\nPlayer 2 type Y to keep your card and N to receive a new card")
    while i < 5:
        x = input(f'would you like to keep {handToString(player2[i])} (Y/N) ')
        if x.lower() == 'n':
            player2[i] = deck.pop(0)
            i = i + 1
        elif x.lower() == 'y':
            i = i + 1
        else:
            print("Please enter either Y or N ")
    bubbleSort(player1)
    bubbleSort(player2)
    print(f"Player 1's hand is {handToString(player1)}")
    print(f"Player 2's hand is {handToString(player2)}")
    p1Hand = findHand(player1)
    p2Hand = findHand(player2)
    print(f"player 1: {p1Hand} player 2: {p2Hand}")
    if p1Hand > p2Hand:
        print("Player 1 wins")
    elif p2Hand > p1Hand:
        print("Player 2 wins")
    else:
        print("Tie")

def findHand(hand):
    #7 Full House
    if (suit(hand[0]) == suit(hand[1])) and suit(hand[3]) == suit(hand[4]) and \
       (suit(hand[2]) == suit(hand[0]) or suit(hand[2]) == suit(hand[4])):
        return 7
     
    #6 Flush
    sameSuit = True
    suitValue = suit(hand[0])
    for i in range (1,5):
        sameSuit = (suitValue == suit(hand[i]))
        if sameSuit == False:
            break
    if sameSuit:
        return 6
    # Straight
    isOrdered = True
    i = 0
    for i in range(0,4):
        if(value(hand[i]) != value(hand[i+1]-1)):
            isOrdered = False
    if isOrdered:
        return 5
    # Three of a kind
    i = 0
    for i in range(0,3):
        if(value(hand[i]) == value(hand[i + 1]) and value(hand[i]) \
           == value(hand[i+2])):
            return 4
    #Two pairs 
    numPairs = 0
    i = 0
    for i in range(0,4):
        if(value(hand[i]) == value(hand[i+1])):
            numPairs = numPairs + 1
        if numPairs == 2:
            return 3
        if numPairs == 1:
            return 2
    return 1

def handToString(cloneDeck):
    suit = ['C','D','H','S']
    val = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    newD = [0 for y in range(52)]
    count = 0
    for i in range(0,4):#Four suits
        for j in range(0,13):#A-K face values
            newD[count] = val[j] + suit[i]
            count = count + 1
    deck = []
    try:
        deck = cloneDeck.copy() #must use .copy() otherwise both would point 
    #to the same memory address and the functions performed would on the 
    #argument would be irreversible and the original integer list would
    #be lost
    except AttributeError:
        deck = cloneDeck #.copy() causes an error if the data type is int
        deck = newD[cloneDeck - 1]
        return deck
    for a in range (0,5):
        deck[a] = newD[deck[a] - 1]
        #deck has values ranging from 1-52
        #newD is a list with 52 string values
        #the correct string value will be the value of newD at the value of 
        #deck - 1 because the indexes are 1 less than the values
    return deck

def suit(num):
    count = 0
    rv = "C"
    while num > 13:
        num = num - 13
        count = count + 1
    if count == 1:
        rv = "D"
    if count == 2:
        rv = "H"
    if count == 3:
        rv = "S"
    return rv

def value(num):
    while num > 13:
        num = num -13
    return num

def main():
    deck = pokerMethod.initialize()
    shuffle(deck)
    play(deck)

main()