#-------------------------------------------------------------------------------
# Name:        Petar Petkovic
# Purpose:     Blackjack
# Author:      petkp9433
# Copyright:   (c) petkp9433 2013
#-------------------------------------------------------------------------------

#imports graphics, time and random libraries to be used
from graphics import*
import random
import time

#function to initialize the starting amount
def start_Amount():
    #set amount of 1000 for the bank, once the game begins
    amount = 1000
    return amount

#draws the betting boxes, checks if the player clicked on them, and puts the
#value into the "bet" box on the screen
def betting_Draw(win,amount):
    #variable holding which place will be chosen from the numbers list
    place = 0
    #a list holding the values able to be bet
    number = ["1","5","25","50","100"]
    #the x-coordinates of the boxes for the values
    x_coords = [[100,145],[151,196],[202,247],[253,298],[304,349],[304,349]]
    #x and y coordinate used for the boxes that have the values to be drawn
    x = 100
    y = 560
    #the x-coordinate for the numbers that are going to be in the boxes
    word = 120
    #initializing a variable to hold the value of the bet
    value = 0
    #draws the 5 boxes with their values in them
    for i in range(5):
        B_Box = Rectangle(Point(x,y), Point(x+45,y+30))
        B_Box.setFill('yellow')
        B_Box.draw(win)
        B_Status = Text(Point(word,y+15),number[place])
        B_Status.draw(win)
        #adds 51 to the box's x-coordinate so it's 51 away from the previous box
        x += 51
        #adds 52 so that the words' x-coordinates are 52 away from the last one
        word += 52
        #adds one so that the value in the boxes are different for each box
        place += 1
    #draws a box for the bank(amount of money the player has)
    bank = Rectangle(Point(375,560),Point(475,590))
    #first one puts the amount the player has in their bank, and the second writes
    #that that box is for the bank
    amount_Bank,write_Bank = Text(Point(425,575),amount), Text(Point(400,550),"Bank:")
    bank.setFill('white')
    #draws the bank box, the amont in it, and the word Bank above it
    bank.draw(win),amount_Bank.draw(win),write_Bank.draw(win)
    #creates a betting button, and a box where the bet value is going to be
    betting_Box,place_Bet = Rectangle(Point(20,560),Point(65,590)),Rectangle(Point(15,500),Point(85,530))
    betting_Box.setFill('white'),place_Bet.setFill('yellow')
    #writes the word bet above the bet box, puts the bet amount in the bet box,
    #and writes "Place Bet" on the betting button
    betting_Status,bet_Amount,write_Bet = Text(Point(40,550),"Bet"),Text(Point(40,575), value),Text(Point(80,515),"Place Bet (min $1)")
    betting_Box.draw(win),betting_Status.draw(win),bet_Amount.draw(win),place_Bet.draw(win),write_Bet.draw(win)
    #initializes a variable to be false
    stop = False
    #to get a click, or multiple until the user places a bet
    while True:
        #checks to see if the program should stop
        if stop == True:
            break
        #gets a mouse click
        p = win.getMouse()
        #a range, to see where the player clicked, what amounts the player wants to bet
        for x in range(5):
            #checks to see if the what value the player clicked to bet
            if p.getX() >= x_coords[x][0] and p.getX() <= x_coords[x][1] and p.getY() >= 560 and p.getY() <= 590:
                #depending on where the player clicked it adds the number to the value
                #variable and takes away the value from the amount, which is the players
                #bank
                value += int(number[x])
                amount -= int(number[x])
                #checks to see if the player tried betting more than the amount
                #that was in the bank
                if amount < 0:
                    #if the amount would go under 0, then the amount clicked is taken
                    #away from the value and put back into the amount, which is the bank
                    #to ensure that the player doesn't bet more than there is in the bank
                    value -= int(number[x])
                    amount += int(number[x])
                    #makes the bank amount how ever much was there before the player
                    #treid to bet more than they had
                    bet_Amount.setText(value),amount_Bank.setText(amount)
                #makes the bank number the amount that the player has
                bet_Amount.setText(value),amount_Bank.setText(amount)
            else:
                #checks to see if the player pressed on the "place bet" button
                if p.getX() >= 15 and p.getX() <= 85 and p.getY() >= 500 and p.getY() <= 530:
                    #if they did, then it checks to see if the bet value is greater
                    #than 0, because the minimum bet is 1$
                    if value > 0:
                        #if it is, then the stop variable is changed to true, making
                        #the program go out of the while loop
                        stop = True
                    else:
                        #if the value is not greater than 0, then the program goes in
                        #the while loop again, until the bet value is more than 0
                        stop = False
    #returns the amount in the bank, the value that was bet, and the two variables
    #which are used to draw those values(bet_Amount,amount_Bank)
    return amount,bet_Amount,amount_Bank,value

#gets the list of cards, with values and returns them
def allCards():
    #creates the cards list, the values that go with the cards and the suits as well
    cards = ["1","6","6","6","6","6","7","7","7","7","7","7","7"]
    values = [1,6,6,6,6,6,7,7,7,7,7,7,7]
    suits = ["c","d","h","s"]
    return cards,values,suits

#function to deal the cards, which puts them in lists to be called on and used later
def dealCards(win,c,v,s):
    #two empty lists
    rcards = []
    rsuits = []
    #picks random nmbers from 0-12 and 0-3 51 times, and makes two lists,
    #one with numbers 0-3 and the other with numbers 0-12
    for i in range(52):
        r = random.randint(0,12)
        r1 = random.randint(0,3)
        rcards.append(r)
        rsuits.append(r1)
    #a variable to be used for the position from the lists
    position = 0
    #two strings, it is to ensure that two decks are used (max 2 of each card)
    chosenCards = ""
    chosenCards1 = ""
    #two empty lists which will be filled with with the suits of the cards,
    #or the actual card itself
    pick_List = []
    suit_List = []
    #as long as the position is not 51 it will run this and once it's 51 it will stop
    while position != 51:
        #picks random cards
        pick, suit= c[rcards[position]],s[rsuits[position]]
        #show creates a string to be checked with the two strings above to check
        #how many times a card has been used
        show = suit + pick + ".gif"
        #checks if the card is in the first string
        if show in chosenCards:
            #checks to see if the card is in the second string
            if show in chosenCards1:
                #if it is it adds one to the counter and goes back into the loop
                position += 1
            #if it's not in the second string, it goes here
            else:
                #puts card into that string
                chosenCards1 += show
                #puts pick into pick list and suit into suit list to be used later
                pick_List.append(pick)
                suit_List.append(suit)
                #adds one to position
                position += 1
        #if the card isn't inside the first string, then goes here
        else:
            #adds the card into the string
            chosenCards += show
            #adds the pick into pick list and suit into suit list
            pick_List.append(pick)
            suit_List.append(suit)
            #adds one to the counter
            position += 1
    #sends back two lists to be chosen from
    return pick_List,suit_List,chosenCards

#function to draw cards, which actually does a whole lot more than expected
def drawCards(win,pick_List,suit_List,chosenCards,v,c):
    #sets a whole bunch of variables to 0, and one to false so that they can
    #be used as counters
    insurance_Ace = False
    Dblack_Jack = 0
    Pblack_Jack = 0
    dealer_Ace = 0
    player_Ace = 0
    done_Once = 0
    dealer_Value = 0
    player_Value = 0
    c1 = 0
    c2 = 0
    #the x and y coordinates for the player and the dealer to draw their cards
    #and boxes for the values that the cards give them
    playerx = 325
    playery = 100
    dealerx = 75
    dealery = 100
    #makes the dealer value box
    D_Box = Rectangle(Point(150,15), Point(180,40))
    D_Box.setFill('white')
    D_Box.draw(win)
    D_Status = Text(Point(165,28),"")
    D_Status.draw(win)
    #makes the player value box
    P_Box = Rectangle(Point(375,15), Point(405,40))
    P_Box.setFill('white')
    P_Box.draw(win)
    P_Status = Text(Point(390,28),"")
    P_Status.draw(win)
    #makes the status box which will tell if the player/dealer, busts, wins, loses etc.
    status_Box = Rectangle(Point(125,300), Point(375,350)) #100 , 225 , 325, 350
    status_Box.setFill('white')
    status_Box.draw(win)
    Status = Text(Point(250,325),"")
    Status.draw(win)
    #makes the program wait 0.5 seconds before dealing the first card after the
    #window is first shown
    time.sleep(0.5)
    #takes the first from the suit list, and pick list and creates the name of
    #the name of the card that's going to be chosen as a string
    show = "Cards/" + (suit_List[0] + pick_List[0] + ".gif")
    #checks to see if there is an ace
    if c.index(pick_List[0]) == 0:
        #sets the ace value at 11
        card1_Value = v[c.index(pick_List[0])] + 10
        #adds one to the counter
        dealer_Ace += 1
    #if there isn't an ace
    else:
        #gets the card and takes its value
        card1_Value = v[c.index(pick_List[0])]
    #Cards/b1fv.gif shows the face down card
    pCard1 = Image(Point(dealerx,dealery), "Cards/b1fv.gif").draw(win)
    time.sleep(0.25)
    #takes the first from the suit list, and pick list and creates the name of
    #the name of the card that's going to be chosen as a string
    show = "Cards/" + (suit_List[1] + pick_List[1] + ".gif")
    c1 = pick_List[1]
    #checks if there is an ace
    if c.index(pick_List[1]) == 0:
        #if there is an ace, sets the value of it to 11 and adds it to the players value
        player_Value += v[c.index(pick_List[1])] + 10
        #adds one to the ace counter
        player_Ace += 1
    #if there isn't an ace
    else:
        #takes the value of the card and adds it to the players value
        #sets a variable to be the value of the card so it can be used to check splitting
        player_Value += v[c.index(pick_List[1])]
    #draws the card
    pCard1 = Image(Point(playerx,playery), show).draw(win)
    time.sleep(0.25)
    #takes the first from the suit list, and pick list and creates the name of
    #the name of the card that's going to be chosen as a string
    show = "Cards/" + (suit_List[2] + pick_List[2] + ".gif")
    #checks to see if the cards an ace
    if c.index(pick_List[2]) == 0:
        #sets the ace value to 11 and adds it to the dealers value
        dealer_Value += v[c.index(pick_List[2])] + 10
        #adds one to the ace counter for dealer
        dealer_Ace += 1
        #if it is an ace then makes the insurance_Ace variable return True(equal to True)
        insurance_Ace = True
    #if the card isn't an ace
    else:
        #adds the value of the card to the dealer value
        dealer_Value += v[c.index(pick_List[2])]
    #draws the card
    pCard2 = Image(Point(dealerx+15,dealery), show).draw(win)
    time.sleep(0.25)
    #takes the first from the suit list, and pick list and creates the name of
    #the name of the card that's going to be chosen as a string
    show = "Cards/" + (suit_List[3] + pick_List[3] + ".gif")
    c2 = pick_List[3]
    #checks to see if the card is an ace
    if c.index(pick_List[3]) == 0:
        #makes it 11 and adds it to the player value
        player_Value += v[c.index(pick_List[3])] + 10
        #adds one to the ace counter for player
        player_Ace += 1
    #if the card isn't an ace
    else:
        #adds the card value to the player value
        #sets a variable to the value of the card so it can be used for splitting
        player_Value += v[c.index(pick_List[3])]
    #draws the card
    pCard2 = Image(Point(playerx+15,playery), show).draw(win)
    time.sleep(0.25)
    #adds the hidden card to the dealer value to check for blackjack
    actual_DValue = (dealer_Value + card1_Value)
    #shows the player and dealer values
    D_Status.setText(dealer_Value)
    P_Status.setText(player_Value)
    #checks to see if the player has blackjack or not, if yes then 1 is added to the
    #counter
    if player_Value == 21:
        Pblack_Jack += 1
    #if the player doesn't have blackjack then it checks if the dealer does
    else:
        #if the dealer has blackjack then one is added to the counter
        if actual_DValue == 21:
            Dblack_Jack += 1
    #checks to see if the dealer is over 21, and if there is an ace
    if dealer_Value > 21 and dealer_Ace > 0:
        #if there is, then it takes 10 away from the total value
        dealer_Value -= 10
        done_Once += 1
        #shows the player and dealer values
        D_Status.setText(dealer_Value)
        P_Status.setText(player_Value)
    #does the same thing as above just for the player
    #checks to see if the player is over 21,
    elif player_Value > 21 and player_Ace > 0:
        #if it is then 10 is taken away from the total value
        player_Value -= 10
        #1 is added to the counter
        done_Once += 1
        #shows the player and dealer values
        P_Status.setText(player_Value)
        D_Status.setText(dealer_Value)
    #so there isn't a hanging "elif"
    else:
        print()
    #returns a lot of variables!(less than before, since the lists arn't being returned
    #since they're mutable!
    return dealer_Value,player_Value,dealer_Ace,player_Ace,Pblack_Jack,Dblack_Jack,Status,P_Status,D_Status,insurance_Ace,card1_Value,done_Once,c1,c2

#checks to see if the player has blackjack or not
def blackJack(win,Pblack_Jack,Status,amount,bet_Amount,amount_Bank,value):
    #makes done false
    done = False
    #makes two variable 0
    reset = 0
    new_Amount_Pjack = 0
    #checks if the player blackjack variable is greater than 0
    if Pblack_Jack > 0:
        #if it is it goes and shows that player has blackjack
        Status.setText("PLAYER BLACKJACK!")
        #waits 3 seconds so the player can read what is going on in the game so it
        #flows nicely
        time.sleep(3)
        #pays out the player 3-1(so if the player bets 100, they get what they started with
        #plus 200)
        new_Amount_Pjack = amount+value*3
        #makes the bet value 0
        bet_Amount.setText(reset)
        #changes the value in the bank to how much they have now since they won
        amount_Bank.setText(new_Amount_Pjack)
        #makes the done variable true
        done = True
    return done,new_Amount_Pjack

#checks and deals with insurance!
def insurance(win,done,insurance_Ace,value,amount_Bank,amount,Dblack_Jack,Status,pick_List,suit_List,bet_Amount):
    #sets two variables to 0
    reset = 0
    new_Amount_Djack = 0
    #checks to make sure done is false which means that the player doesn't have blackjack
    if done == False:
        #checks if the dealer has an ace showing
        if insurance_Ace == True:
            #draws insurance on the screen, and a white box saying how much
            #the insurance is worth
            insurance = Text(Point(325,425),"Insurance?")
            insurance.draw(win)
            insurance_Amount = Rectangle(Point(400,450),Point(450,480))
            insurance_Amount.setFill('white')
            insurance_Amount.draw(win)
            #calculates the insurance value and puts it into the insurance box
            ins_value = (value//2)
            Insurance_Amount = Text(Point(425,465),(ins_value))
            Insurance_Amount.draw(win)
            #creates the yer and no buttons
            yes_Box,no_Box = Rectangle(Point(370,410),Point(420,440)),Rectangle(Point(430,410),Point(480,440))
            Yes_Box = Text(Point(395,425),"Yes")
            No_Box = Text(Point(455,425),"No")
            yes_Box.setFill('yellow')
            no_Box.setFill('yellow')
            #draws the yes and no buttons
            yes_Box.draw(win),no_Box.draw(win),Yes_Box.draw(win),No_Box.draw(win)
            #this is to check if the player clicks on the yes or no button and doesn't
            #stop until one of them is clicked
            while True:
                #gets a mouse click
                p = win.getMouse()
                #checks to see if the user pressed yes to insurance
                if p.getX() >= 370 and p.getX() <= 420 and p.getY() >=410 and p.getY() <=440:
                    #checks to see if the dealer has blackjack
                    if Dblack_Jack > 0:
                        #if the dealer does, then it shows the face down card
                        show = "Cards/" + (suit_List[0] + pick_List[0] + ".gif")
                        pCard1 = Image(Point(75,100),show).draw(win)
                        show = "Cards/" + (suit_List[2] + pick_List[2] + ".gif")
                        pCard1 = Image(Point(90,100),show).draw(win)
                        #the status bar says that the dealer has blackjack
                        Status.setText("DEALER BLACKJACK!")
                        #program waits for 3 seconds so that the player can realize
                        #what has just happened and so it's smoothe
                        time.sleep(3)
                        #makes the new amount equal to the amount before the bet was made
                        #taking away how much insurance was offered
                        new_Amount_Djack = amount+value-ins_value
                        #sets the bank amount to the new bank amount calculated
                        amount_Bank.setText(new_Amount_Djack)
                        #resets the bet amount
                        bet_Amount.setText(reset)
                        #sets done to True
                        done = True
                        #undraws the insurance, the yes and no boxes and the insurance box/value in it
                        insurance.undraw(),insurance_Amount.undraw(),yes_Box.undraw(),no_Box.undraw(),Yes_Box.undraw(),No_Box.undraw(),Insurance_Amount.undraw()
                        #goes out of the while loop
                        break
                    #if the dealer doesn't have blackjack
                    else:
                        #takes away the insurance amount from the bank
                        amount_Bank.setText(amount-ins_value)
                        #sets done to False
                        done = False
                        #undraws the insurance, the yes and no boxes and the insurance box/value in it
                        insurance.undraw(),insurance_Amount.undraw(),yes_Box.undraw(),no_Box.undraw(),Yes_Box.undraw(),No_Box.undraw(),Insurance_Amount.undraw()
                        break
                else:
                    #if the player doesn't click that they want insuracne then goes here
                    if p.getX() >= 430 and p.getX() <= 480 and p.getY() >=410 and p.getY() <=440:
                        #undraws the insurance, the yes and no boxes and the insurance box/value in it
                        insurance.undraw(),insurance_Amount.undraw(),yes_Box.undraw(),no_Box.undraw(),Yes_Box.undraw(),No_Box.undraw(),Insurance_Amount.undraw()
                        #sets done to False
                        done = False
                        #breaks out of the while loop
                        break
    return done,new_Amount_Djack

def splitting_Check(win,c1,c2):
    double_Cards = False
    if c1 == c2:
        double_Cards = True
    return double_Cards

def splitting_DrawYesorNo(win,double_Cards):
    if double_Cards == True:
        split = Text(Point(50,275),"Split?")
        split.draw(win)
        yes_Box,no_Box = Rectangle(Point(10,290), Point(90,330)), Rectangle(Point(10,340), Point(90,380))
        Yes_Box = Text(Point(50,310),"Yes")
        No_Box = Text(Point(50,360),"No")
        yes_Box.setFill('yellow')
        no_Box.setFill('yellow')
        #draws the yes and no buttons
        yes_Box.draw(win),no_Box.draw(win),Yes_Box.draw(win),No_Box.draw(win)
        return yes_Box,no_Box,Yes_Box,No_Box,split
    else:
        if double_Cards == False:
            return 1,2,3,4,5

def splitting_ClickYesorNo(win,double_Cards):
    Split = False
    if double_Cards == True:
        while True:
            p = win.getMouse()
            x,y = p.getX(),p.getY()
            if x >= 10 and x <= 90 and y >= 290 and y <= 330:
                Split = True
                break
            else:
                if p.getX() >= 10 and p.getX() <= 90 and p.getY() and p.getY() >= 340 and p.getY() <= 380:
                    Split = False
                    break
    return Split

def splitting_Hide(win,yes_Box,no_Box,Yes_Box,No_Box,split,double_Cards):
    if double_Cards == True:
        yes_Box.undraw(),no_Box.undraw(),Yes_Box.undraw(),No_Box.undraw(),split.undraw()

def split_Draw(win,pick_List,suit_List,Split,double_Cards):
    if double_Cards == True:
        top_playerx = 325
        top_playery = 100
        bot_playerx = 325
        bot_playery = 200
        if Split == True:
            #takes the first from the suit list, and pick list and creates the name of
            #the name of the card that's going to be chosen as a string
            show = "Cards/" + (suit_List[3] + pick_List[3] + ".gif")
            #draws the card
            pCard2 = Image(Point(bot_playerx,bot_playery), show).draw(win)
            cover_Card = Rectangle(Point(305,52), Point(375,147))
            cover_Card.setFill('green')
            cover_Card.setOutline('green')
            cover_Card.draw(win)
            #takes the first from the suit list, and pick list and creates the name of
            #the name of the card that's going to be chosen as a string
            show = "Cards/" + (suit_List[1] + pick_List[1] + ".gif")
            #draws the card
            pCard1 = Image(Point(top_playerx,top_playery), show).draw(win)

def check_cards(pick_List,c,v,Split,double_Cards):
    first_Value = 0
    second_Value = 0
    if double_Cards == True:
        if Split == True:
            if c.index(pick_List[1]) == 0:
                #sets the ace value at 11
                first_Value += v[c.index(pick_List[1])] + 10
            #if there isn't an ace
            else:
                #gets the card and takes its value
                first_Value = v[c.index(pick_List[1])]
            if c.index(pick_List[3]) == 0:
                #sets the ace value at 11
                second_Value += v[c.index(pick_List[3])] + 10
            #if there isn't an ace
            else:
                #gets the card and takes its value
                second_Value = v[c.index(pick_List[3])]
    return first_Value,second_Value

def split_Values(win,c,v,first_Value,second_Value,P_Status,Split):
    second_Box = Rectangle(Point(375,255), Point(405,280))
    second_Box.setFill('white')
    second_Status = Text(Point(390,268),second_Value)
    if Split == True:
        P_Status.setText(first_Value)
        second_Box.draw(win)
        second_Status.draw(win)
    return second_Status

def split_Status(win,Split):
    top_box,bot_box = Rectangle(Point(420,15),Point(475,40)),Rectangle(Point(420,255),Point(475,280))
    top_box.setFill('white'),bot_box.setFill('white')
    top_Status,bot_Status = Text(Point(448,28),""),Text(Point(448,268),"")
    if Split == True:
        top_box.draw(win),bot_box.draw(win)
        top_Status.draw(win),bot_Status.draw(win)
    return top_Status,bot_Status

#checks to see if the player busted, meaning that the dealer won
def is_Bust(win,bust,Status,Stand_Box,Hit_Box,amount,bet_Amount,amount_Bank):
    #two variables set to a value of 0
    reset = 0
    new_Amount = 0
    #if the bust counter is 1 then it goes inside
    if bust == 1:
        #setst the status box to the player busted and dealer wins
        Status.setText("PLAYER BUSTED, DEALER WINS")
        #stops the program for two second for player to realize what happened
        time.sleep(2)
        #resets the bet amount and changes the new amount that the player has in his bank
        bet_Amount.setText(reset)
        #makes amount whatever the player has now in their bank
        new_Amount = amount
        amount_Bank.setText(new_Amount)
    return new_Amount,bust

#this is a function for the players turn, while the player hits "hit" or "stand"
def playerTurn(win,player_Value,player_Ace,pick_List,suit_List,c,v,P_Status,done_Once,Split,top_Status,bot_Status):
    hand = 0
    #the x and y coordinates
    #creates the hit and stand buttons
    hit_Box = Rectangle(Point(410,290), Point(490,330))
    hit_Box.setFill('yellow')
    hit_Box.draw(win)
    Hit_Box = Text(Point(450,310),"Hit")
    Hit_Box.draw(win)
    stand_Box = Rectangle(Point(410,340), Point(490,380))
    stand_Box.setFill('yellow')
    stand_Box.draw(win)
    Stand_Box = Text(Point(450,360),"Stand")
    Stand_Box.draw(win)

    #stand, bust counters, and hold the number of moves
    move = 4
    stand = 0
    bust = 0

    playerx = 355
    playery = 100
    #checks for a click(hit, or stand)
    while True:
        if Split == True:
            if hand == 0:
                playerx = 340
                playery = 100
            else:
                if hand == 1:
                    playerx = 340
                    playery = 200
                elif stand > 0:
                    playerx = 340
                    playery = 200
                else:
                    if bust > 0:
                        playerx = 340
                        playery = 200
        p = win.getMouse()
        #makes sure that the player didn't stand, bust or get blackjack
        if stand > 0:
            break
        elif bust > 0:
            break
        #checks to see if the user clicked the hit button
        elif p.getX() >= 410 and p.getX() <= 490 and p.getY() >=290 and p.getY() <=330:
            show = "Cards/" + (suit_List[move] + pick_List[move] + ".gif")
            #checks if the card is an ace
            if c.index(pick_List[move]) == 0:
                #if it's the first ace or no aces yet, the ace value is set to 10
                #if that makes the player's value go over 21 then it is reduced
                #and the ace value is only 1
                if player_Ace == 0 or player_Ace == 1:
                    player_Value += v[c.index(pick_List[move])] + 10
                    if player_Value > 21:
                        #takes away 10 if the ace being 11 makes the player bust
                        player_Value -= 10
                        #adds one to the done once counter
                        done_Once += 1
                        #if that makes the player have 21 then 1 is added to the
                        #stand counter
                        if player_Value == 21:
                            time.sleep(1)
                            stand += 1
                            if hand == 0:
                                top_Status.setText("Stand")
                                hand += 1
                            else:
                                if hand == 1:
                                    bot_Status.setText("Stand")
                                    hand += 1
                        else:
                            break
                #if theres more than 1 ace then it goes here
                else:
                    #gives the player the value of the card
                    player_Value += v[c.index(pick_List[move])]
                    #checks to see if the player has 21
                    if player_Value == 21:
                        stand += 1
                        if hand == 0:
                            top_Status.setText("Stand")
                            hand += 1
                        else:
                            if hand == 1:
                                bot_Status.setText("Stand")
                                hand += 1
                        time.sleep(1)
                    #checks to see if the player busted (over 21)
                    else:
                        if player_Value > 21:
                            #adds one to the bust counter
                            bust += 1
                            pCard1 = Image(Point(playerx,playery), show).draw(win)
                            P_Status.setText(player_Value)
                            if Split == True:
                                if hand == 0:
                                    top_Status.setText("Bust")
                                    hand += 1
                                else:
                                    if hand == 1:
                                        bot_Status.setText("Bust")
                                        hand += 1
                            else:
                                break

                #adds one to the ace counter
                player_Ace += 1
            #if the card drawn isn't an ace
            else:
                #takes the card and the value and adds it to the player value
                pCard1 = Image(Point(playerx,playery), show).draw(win)
                player_Value += v[c.index(pick_List[move])]
                P_Status.setText(player_Value)
                #checks to see if player has 21
                if player_Value == 21:
                    time.sleep(1)
                    stand += 1
                    if Split == True:
                        if hand == 0:
                            top_Status.setText("Stand")
                            hand += 1
                        else:
                            if hand == 1:
                                bot_Status.setText("Stand")
                                hand += 1
                    else:
                        break
                #checks to see if the player busted (over 21)
                elif player_Value > 21:
                    #if the player did and the player has 1 ace, and it hasn't
                    #been done before it takes 10 away from the total value so
                    #that the ace is counted as 1 instead of 11 causing a bust
                    if player_Ace == 1:
                        if done_Once == 0:
                            player_Value -= 10
                            #adds one to the counter
                            done_Once += 1
                        #if it's been done already once then it doesn't do it again
                        else:
                            #adds one to the bust counter
                            bust += 1
                            pCard1 = Image(Point(playerx,playery), show).draw(win)
                            #makes the status whatever the player value is
                            P_Status.setText(player_Value)
                            if Split == True:
                                if hand == 0:
                                    top_Status.setText("Bust")
                                    hand += 1
                                else:
                                    if hand == 1:
                                        bot_Status.setText("Bust")
                                        hand += 1
                            else:
                                break
                    #if the player doesn't have one ace or more than one ace then
                    #it goes here, adds one to the bust counter and shows the card
                    else:
                        bust += 1
                        pCard1 = Image(Point(playerx,playery), show).draw(win)
                        P_Status.setText(player_Value)
                        if Split == True:
                            if hand == 0:
                                top_Status.setText("Bust")
                                hand += 1
                            else:
                                if hand == 1:
                                    bot_Status.setText("Bust")
                                    hand += 1
                        else:
                            break
                #if the done_Once counter is 0 then it goes here to see if there
                #is one ace, and if that one ace makes it over 21(bust) then it
                #takes 10 from the player value making the ace worth 1
                else:
                    if done_Once == 0:
                        if player_Ace == 1:
                            if player_Value > 21:
                                player_Value -= 10
                                #adds one to the couner
                                done_Once += 1

            #shows the card and the value of it is shown
            pCard1 = Image(Point(playerx,playery), show).draw(win)
            P_Status.setText(player_Value)
            #adds 15 to the x coordiante for the player
            playerx += 15
            #adds one to the move counter
            move += 1
        #if the player clicks on the stand button then it goes here and adds one
        #to the stand counter
        else:
            if p.getX() >= 410 and p.getX() <= 490 and p.getY() >=340 and p.getY() <=380:
                stand += 1
                time.sleep(0.25)
                if Split == True:
                    if hand == 0:
                        top_Status.setText("Stand")
                        hand += 1
                    else:
                        if hand == 1:
                            bot_Status.setText("Stand")
            else:
                break
    #returns a few variables!
    return bust,stand,move,player_Value,Stand_Box,Hit_Box

#this is a function for the dealers turn adding cards until eiter between 17 and 21, or over 21
def dealerTurn(win,dealer_Value,dealer_Ace,pick_List,suit_List,c,v,stand,move,D_Status,card1_Value):
    #the x and y coordinates
    dealerx = 105
    dealery = 100
    #two counters that are needed set to 0
    bust = 0
    done_Once = 0
    #checks if the player pressed the stand button
    if stand > 0:
        #shows the card that was face down
        show = "Cards/" + (suit_List[0] + pick_List[0] + ".gif")
        pCard1 = Image(Point(75,dealery),show).draw(win)
        show = "Cards/" + (suit_List[2] + pick_List[2] + ".gif")
        pCard1 = Image(Point(90,dealery),show).draw(win)
        #adds the value of the facedown card and puts it on the dealer status box
        dealer_Value += card1_Value
        #if the cards an ace and there is already an ace then the value is put to 1
        if dealer_Value > 21 and dealer_Ace > 0:
            dealer_Value -= 10
            D_Status.setText(dealer_Value)
        else:
            D_Status.setText(dealer_Value)
        #as long as the dealer value is less than 17 it goes through
        while dealer_Value < 17:
            #makes it wait one second so that the cards don't show up too quickly
            #gives the user a second to realize what card the dealer got
            #makes the game a little bit more realistic
            time.sleep(1)
            show = "Cards/" + (suit_List[move] + pick_List[move] + ".gif")
            #checks to see if it's an ace and if there are any other aces present
            if c.index(pick_List[move]) == 0:
                if dealer_Ace == 0 or dealer_Ace == 1:
                    #if there is and the value is over 21 then the value is reduced
                    #to the ace only having a value of 1
                    dealer_Value += v[c.index(pick_List[move])] + 10
                    if dealer_Value > 21:
                        #takes 10 away from the dealer value
                        dealer_Value -= 10
                        #adds one to the done once counter
                        done_Once += 1
                #if it isn't the first ace then it goes here
                else:
                    #makes the ace worth 1 and checks to see if it makes the value
                    #over 21, or equal to 21 adding to the appropriate counter
                    dealer_Value += v[c.index(pick_List[move])]
                    if dealer_Value > 21:
                        #adds one to the bust counter
                        bust += 1
                        pCard1 = Image(Point(dealerx,dealery), show).draw(win)
                        D_Status.setText(dealer_Value)
                dealer_Ace += 1
            #if the card drawn isn't an ace then it goes here
            else:
                #gets the card and adds the value
                pCard1 = Image(Point(dealerx,dealery), show).draw(win)
                dealer_Value += v[c.index(pick_List[move])]
                #shows the value in the status box
                D_Status.setText(dealer_Value)
                #if it's over 21, and there is only 1 ace then it takes 10 away
                #from the dealer value
                if dealer_Value > 21:
                    if dealer_Ace == 1:
                        #checks if it's been done, if it hasn't then it takes 10
                        #away from the total value
                        if done_Once == 0:
                            dealer_Value -= 10
                            #adds one to the done once counter
                            done_Once += 1
                        else:
                            #if it's already been done then it shows the cards
                            #and adds one to the bust counter
                            bust += 1
                            pCard1 = Image(Point(dealerx,dealery), show).draw(win)
                            D_Status.setText(dealer_Value)
                    #if there isn't exactly one ace, then the dealer busts, it shows
                    #the card and adds the value
                    else:
                        #adds one to the bust counter
                        bust += 1
                        pCard1 = Image(Point(dealerx,dealery), show).draw(win)
                        D_Status.setText(dealer_Value)
                #checks if the counter is at 0, if it is then it checks to see
                #if there is an ace or not. If there is one ace 10 is taken away
                #from the dealer value so the ace is worth only 1, making the dealer
                #not bust
                else:
                    if done_Once == 0:
                        if dealer_Ace == 1:
                            if dealer_Value > 21:
                                dealer_Value -= 10
                                #adds one to the counter
                                done_Once += 1

            #shows the card and the value the dealer has
            pCard1 = Image(Point(dealerx,dealery), show).draw(win)
            D_Status.setText(dealer_Value)
            #adds 15 to the dealer x coordinate
            dealerx += 15
            move += 1
    #returns the dealer value
    return dealer_Value

#this is a function that checks to see who the winner is, and how they won
def winner(win,Status,dealer_Value,player_Value,Hit_Box,Stand_Box):
    #sets a variable to the value of 0
    number = 0
    #checks if the dealer value is greater than the player value making number 0
    #if it isn't then number is 1
    if dealer_Value > player_Value:
        if dealer_Value > 21:
            number += 0
        else:
            number += 1
    else:
        #checks if the player value is greater than the dealer value making number 2
        if player_Value > dealer_Value:
            number += 2
        else:
            if player_Value == dealer_Value:
                number += 3
    #returns the number and status so it can be changed
    return number,Status

def play_Again(win,number,Status,stand,Stand_Box,Hit_Box,amount,bet_Amount,amount_Bank,value,Dblack_Jack):
    #sets two variables to 0
    reset = 0
    new_Amount = 0
    #making sure that the stand counter has atleast one in it(meaning the player
    #pressed the stand button) it goes here
    if stand > 0:
        #dependant on what number was returned a different message is displayed
        #so that the player knows who won, which is shown in the big 'status'
        #box near the middle/bottom of the playing window
        message =["DEALER BUSTS, PLAYER WINS!","DEALER WINS!","PLAYER WINS!","PUSH!","DEALER BLACKJACK!"]
        if Dblack_Jack > 0:
            #makes the status whatever is needed
            Status.setText(message[4])
            #makes the program wait 2 seconds for nice flow of the game
            time.sleep(2)
            #changes the amount to the new amount that's needed for the bank
            new_Amount = amount
            #resets the bet value to 0
            bet_Amount.setText(reset)
            amount_Bank.setText(new_Amount)
        elif message[number] == "DEALER BUSTS, PLAYER WINS!" or message[number] == "PLAYER WINS!":
            #makes the status whatever is needed
            Status.setText(message[number])
            #program waits 2 seconds
            time.sleep(2)
            #makes the new amount the amount + 2 times whatever was bet
            new_Amount = amount+value*2
            #resets the bet value
            bet_Amount.setText(reset)
            amount_Bank.setText(new_Amount)
        elif message[number] == "DEALER WINS!":
            #makes the status whatever is needed
            Status.setText(message[number])
            #program waits 2 seconds
            time.sleep(2)
            #makes the new amount equal to what the amount is
            new_Amount = amount
            bet_Amount.setText(reset)
            amount_Bank.setText(new_Amount)
        else:
            if message[number] == "PUSH!":
                #makes the status whatever it needs to be
                Status.setText(message[number])
                #program waits 2 seconds
                time.sleep(2)
                #the new amount in the bank is the amount adding the value that was bet
                new_Amount = amount + value
                #the bet value is reset
                bet_Amount.setText(reset)
                amount_Bank.setText(new_Amount)
        return new_Amount

#for the highscore
def high_Score(win,amount,highscore):
    #draws highscore so the player can see it
    Text(Point(50,420),"HighScore:").draw(win)
    #writes what the highscore is
    score_high = Text(Point(125,420),highscore)
    score_high.draw(win)
    #returns the highscore value
    return score_high

def main():
    #main function, tries so that there isn't a graphics error when pressing 'x'
    #on any of the windows that are open while playing
    try:
        while True:
            #draws the window
            win = GraphWin("Blackjack",500,600)
            box,box_Bet = Rectangle(Point(0,0), Point(500,400)),Rectangle(Point(0,400), Point(500,600))
            box.setFill('green'),box_Bet.setFill('grey')
            #draws the background
            background = box.draw(win),box_Bet.draw(win)
            #takes the amount from the first function
            amount = start_Amount()
            #reads the first line in the file and sets it to highscore
            highscore = int(open("highscore.txt","r").read())
            #has the highscore function show the current highscore
            score_high = high_Score(win,amount,highscore)
            #as long as the bank has more than 0$ in it it will go through
            while amount > 0:
                #prints the amount into the file at the first position
                print(amount, file = open("highscore.txt","w"))
                #checks if highscore is less than the amount in the file
                if highscore <= amount:
                    #if it is less, then the highscore is set to whatever the amount it
                    highscore = amount
                #sets the highscore to the highscore dependant on whether it has chagned or not
                score_high.setText(highscore)
                #draws the betting area
                box,box_Bet = Rectangle(Point(0,0), Point(500,400)),Rectangle(Point(0,400), Point(500,600))
                box.setFill('green')
                box.draw(win),box_Bet.setFill('grey')
                amount,bet_Amount,amount_Bank,value = betting_Draw(win,amount)
                #writes the dealer/player hand so that the user knows
                Text(Point(90,25),"Dealer's Hand:").draw(win),Text(Point(315,25),"Player's Hand:").draw(win)
                #goes through the functions
                c,v,s = allCards()
                pick_List,suit_List,chosenCards = dealCards(win,c,v,s)
                dealer_Value,player_Value,dealer_Ace,player_Ace,Pblack_Jack,Dblack_Jack,Status,P_Status,D_Status,insurance_Ace,card1_Value,done_Once,c1,c2 = drawCards(win,pick_List,suit_List,chosenCards,v,c)
                done,new_Amount_Pjack = blackJack(win,Pblack_Jack,Status,amount,bet_Amount,amount_Bank,value)
                #if the blackjack function returns true, then the amount is set to
                #whatever the amount was in that function and it goes back to the top
                #of the while loop to check if amount is greater than 0
                if done == True:
                    amount = new_Amount_Pjack
                #if it isn't done(aka no blackjack for player)
                else:
                    #goes to insurance
                    done,new_Amount_Djack = insurance(win,done,insurance_Ace,value,amount_Bank,amount,Dblack_Jack,Status,pick_List,suit_List,bet_Amount)
                    #if after insurance it returns True, then again, the amount is set
                    #to the amount in the insurance function and it goes to the top
                    #of the while loop to check if amount is greater than 0
                    if done == True:
                        amount = new_Amount_Djack
                    #if it isn't done(aka no blackjack for dealer)
                    else:
                        #goes through the functions
                        double_Cards = splitting_Check(win,c1,c2)
                        yes_Box,no_Box,Yes_Box,No_Box,split = splitting_DrawYesorNo(win,double_Cards)
                        Split = splitting_ClickYesorNo(win,double_Cards)
                        splitting_Hide(win,yes_Box,no_Box,Yes_Box,No_Box,split,double_Cards)
                        split_Draw(win,pick_List,suit_List,Split,double_Cards)
                        first_Value,second_Value = check_cards(pick_List,c,v,Split,double_Cards)
                        second_Status = split_Values(win,c,v,first_Value,second_Value,P_Status,Split)
                        top_Status,bot_Status = split_Status(win,Split)
                        bust,stand,move,player_Value,Stand_Box,Hit_Box = playerTurn(win,player_Value,player_Ace,pick_List,suit_List,c,v,P_Status,done_Once,Split,top_Status,bot_Status)
                        new_Amount_,bust = is_Bust(win,bust,Status,Stand_Box,Hit_Box,amount,bet_Amount,amount_Bank)
                        dealer_Value = dealerTurn(win,dealer_Value,dealer_Ace,pick_List,suit_List,c,v,stand,move,D_Status,card1_Value)
                        number,Status = winner(win,Status,dealer_Value,player_Value,Stand_Box,Hit_Box)
                        new_Amount = play_Again(win,number,Status,stand,Stand_Box,Hit_Box,amount,bet_Amount,amount_Bank,value,Dblack_Jack)
                        #if the player busted, then an amount it set
                        if bust == 1:
                            amount = new_Amount_
                        #if the player didn't bust then another amount it set
                        else:
                            amount = new_Amount
                #if the amount is 0 then it goes here
                if amount == 0:
                    #breaks out of the while loop
                    break
            #replaces the hit and stand button with "play again" and "quit"
            again_Box,quit_Box = Rectangle(Point(410,290), Point(490,330)),Rectangle(Point(410,340), Point(490,380))
            again_Box.setFill('yellow'),quit_Box.setFill('yellow')
            Again_Box = Text(Point(450,310),"Play Again")
            Quit_Box = Text(Point(450,360),"Quit")
            quit_Box.draw(win),again_Box.draw(win),Quit_Box.draw(win),Again_Box.draw(win)
            Status.setText("GAME OVER!")
            #waits for the player to click
            while True:
                #gets the mouse click
                p = win.getMouse()
                #if the player presses to play again then the window is closed and run again
                #with the highscore staying what it was in the previous game
                if p.getX() >= 410 and p.getX() <= 490 and p.getY() >=290 and p.getY() <=330:
                    win.close()
                    print(highscore, file = open("highscore.txt","w"))
                    main()
                #if the player presses quit then the window closes and the game is over
                else:
                    if p.getX() >= 410 and p.getX() <= 490 and p.getY() >=340 and p.getY() <=380:
                        win.close()
    except GraphicsError:
        print
main()