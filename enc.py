import chess
from random import *
from packets import *  # this imports my packets script so we can use those functions in this script

# global variables for if each space is a 1 or a 0
a1 = 1
b1 = 0
c1 = 1
d1 = 0
e1 = 1
f1 = 0
g1 = 1
h1 = 0
a2 = 0
b2 = 1
c2 = 0
d2 = 1
e2 = 0
f2 = 1
g2 = 0
h2 = 1
a3 = 1
b3 = 0
c3 = 1
d3 = 0
e3 = 1
f3 = 0
g3 = 1
h3 = 0
a4 = 0
b4 = 1
c4 = 0
d4 = 1
e4 = 0
f4 = 1
g4 = 0
h4 = 1
a5 = 1
b5 = 0
c5 = 1
d5 = 0
e5 = 1
f5 = 0
g5 = 1
h5 = 0
a6 = 0
b6 = 1
c6 = 0
d6 = 1
e6 = 0
f6 = 1
g6 = 0
h6 = 1
a7 = 1
b7 = 0
c7 = 1
d7 = 0
e7 = 1
f7 = 0
g7 = 1
h7 = 0
a8 = 0
b8 = 1
c8 = 0
d8 = 1
e8 = 0
f8 = 1
g8 = 0
h8 = 1

# initializes the board as we start the program and which turn it is
board = chess.Board()
turn = "Black"  # set to black cause we'll change before the game starts

# this is our function which gets the move we're going to make
def getmove(digit):
    # we start by getting the move in uci notation- e.g. a3a5 would move a piece from space a3 to space a5
    store = randomletter()  # choses letter first
    store = store + randomnumber()  # choses number second
    second = randomletter()
    second = second + randomnumber()

    # next we make sure the space we move to represents the digit we want to send
    # we do this by comparing the space we chose to the variable of the space we stored above
    # I think that there is probably a better way to do this, but I am not sure how to currently
    if second == "a1":  # checks the space we chose randomly
        if str(a1) != digit:  # we check if the string value of the gobal variable is not equal to the value we had the user input, which is also a string
            return 1  # if it is not equal- this space does not send the digit we want it to, we return from the function with an error
    elif second == "a2":
        if str(a2) != digit:
            return 1
    elif second == "a3":
        if str(a3) != digit:
            return 1
    elif second == "a4":
        if str(a4) != digit:
            return 1
    elif second == "a5":
        if str(a5) != digit:
            return 1
    elif second == "a6":
        if str(a6) != digit:
            return 1
    elif second == "a7":
        if str(a7) != digit:
            return 1
    elif second == "a8":
        if str(a8) != digit:
            return 1
    elif second == "b1":
        if str(b1) != digit:
            return 1
    elif second == "b2":
        if str(b2) != digit:
            return 1
    elif second == "b3":
        if str(b3) != digit:
            return 1
    elif second == "b4":
        if str(b4) != digit:
            return 1
    elif second == "b5":
        if str(b5) != digit:
            return 1
    elif second == "b6":
        if str(b6) != digit:
            return 1
    elif second == "b7":
        if str(b7) != digit:
            return 1
    elif second == "b8":
        if str(b8) != digit:
            return 
    elif second == "c1":
        if str(c1) != digit:
            return 1
    elif second == "c2":
        if str(c2) != digit:
            return 1
    elif second == "c3":
        if str(c3) != digit:
            return 1
    elif second == "c4":
        if str(c4) != digit:
            return 1
    elif second == "c5":
        if str(c5) != digit:
            return 1
    elif second == "c6":
        if str(c6) != digit:
            return 1
    elif second == "c7":
        if str(c7) != digit:
            return 1
    elif second == "c8":
        if str(c8) != digit:
            return 1
    elif second == "d1":
        if str(d1) != digit:
            return 1
    elif second == "d2":
        if str(d2) != digit:
            return 1
    elif second == "d3":
        if str(d3) != digit:
            return 1
    elif second == "d4":
        if str(d4) != digit:
            return 1
    elif second == "d5":
        if str(d5) != digit:
            return 1
    elif second == "d6":
        if str(d6) != digit:
            return 1
    elif second == "d7":
        if str(d7) != digit:
            return 1
    elif second == "d8":
        if str(d8) != digit:
            return 1
    elif second == "e1":
        if str(e1) != digit:
            return 1
    elif second == "e2":
        if str(e2) != digit:
            return 1
    elif second == "e3":
        if str(e3) != digit:
            return 1
    elif second == "e4":
        if str(e4) != digit:
            return 1
    elif second == "e5":
        if str(e5) != digit:
            return 1
    elif second == "e6":
        if str(e6) != digit:
            return 1
    elif second == "e7":
        if str(e7) != digit:
            return 1
    elif second == "e8":
        if str(e8) != digit:
            return 1
    elif second == "f1":
        if str(f1) != digit:
            return 1
    elif second == "f2":
        if str(f2) != digit:
            return 1
    elif second == "f3":
        if str(f3) != digit:
            return 1
    elif second == "f4":
        if str(f4) != digit:
            return 1
    elif second == "f5":
        if str(f5) != digit:
            return 1
    elif second == "f6":
        if str(f6) != digit:
            return 1
    elif second == "f7":
        if str(f7) != digit:
            return 1
    elif second == "f8":
        if str(f8) != digit:
            return 1
    elif second == "g1":
        if str(g1) != digit:
            return 1
    elif second == "g2":
        if str(g2) != digit:
            return 1
    elif second == "g3":
        if str(g3) != digit:
            return 1
    elif second == "g4":
        if str(g4) != digit:
            return 1
    elif second == "g5":
        if str(g5) != digit:
            return 1
    elif second == "g6":
        if str(g6) != digit:
            return 1
    elif second == "g7":
        if str(g7) != digit:
            return 1
    elif second == "g8":
        if str(g8) != digit:
            return 1
    elif second == "h1":
        if str(h1) != digit:
            return 1
    elif second == "h2":
        if str(h2) != digit:
            return 1
    elif second == "h3":
        if str(h3) != digit:
            return 1
    elif second == "h4":
        if str(h4) != digit:
            return 1
    elif second == "h5":
        if str(h5) != digit:
            return 1
    elif second == "h6":
        if str(h6) != digit:
            return 1
    elif second == "h7":
        if str(h7) != digit:
            return 1
    elif second == "h8":
        if str(h8) != digit:
            return 1

    if store == second:  # we also check if we chose the same space twice, because that will cause an error to be thrown and the program to crash
        return 1  # if they are the same, we return from the function with the flag to do it again

    first = store  # used for printing later
    store = store + second  # if they aren't the same, we combine the two strings so we can use it as a move
    x = makemove(store) # we start our makemove() function with the generated move as input
    if x == 1:  # if the makemove() function is unsuccessful
        return 1  # returns the function so we do it again
    elif x == 0:  # the makemove() function is successful
        if turn == "White":  # I think that there may be a way to say something like 'pawn to e4', but I cannot currently think of an easy way to find out what piece is at a certain location, so I'm going to skip that for now
            print("White:", end = " ")  # also we should be able to just say chess.color or chess.WHITE, but I couldn't get that to work
            send = "White: "
        elif turn == "Black":
            print("Black:", end = " ")
            send = "Black: "
        print("Move", first, "to", second)  # print the move we made- this format will likely be changed
        send = send + "Move "
        send = send + first
        send = send + " to "
        send = send + second
        sendchess(send)
        return 0

def printboard():  # function to print the board because I thought it was easier to use this function than remember the syntax for python chess
    print(board)

def randomletter():  # function to choose a random letter for our moves
    x = randint(0, 7)  # randomness
    y = ""  # so we can store the random generated number as a string character for the move

    if x == 0:  # if we get zero, the move will be a-something and so on and so forth
        y = "a"
    elif x == 1:
        y = "b"
    elif x == 2:
        y = "c"
    elif x == 3:
        y = "d"
    elif x == 4:
        y = "e"
    elif x == 5:
        y = "f"
    elif x == 6:
        y = "g"
    elif x == 7:
        y = "h"

    return y  # returns the letter we chose

def randomnumber():  # choosing a random number for the move
    x = randint(1,8)  # chooses a random number in the range
    return str(x)  # returns the string version of the number we chose so it can work in the move format

def makemove(store):  # function which will make the actual move we will do
    move = chess.Move.from_uci(store)  # converts our uci format into a format that python chess understands
    x = move in board.legal_moves  # now we have to check if it's a legal move
    # this is the main reason I chose python chess, because it has a built in ability to see if a move is legal- would have taken a lot of work on my part to do the same
    if x == True:  # if a legal move
        board.push(move)  # executes the move
        print()  # gives us a blank line in out output
        printboard()  # prints the board so we can see that the move was success fun
        return 0  # returns without an issue
    elif x == False:  # if the move isn't legal
        return 1  # we return with the intent to do the whole thing over again

# essentially the main() of the program
printboard()  # prints the board in the starting position
conv = ""  # we'll use this as a string variable later - eventually we'll put this in a loop/function so the user can choose multiple letters/messages to send
uword = input("What word/letter do you want to send?")  # getting what the user wants to send
length = len(uword)  # grabbing the length of the message for later
for x in range (0, length):  # looping through the length of the message and converting it to binary
    temp = ''.join(format(i, 'b') for i in bytearray(uword[x], encoding ='utf-8'))  # actual way to convert each character to binary
    if len(temp) == 7:  # this is used because the above formula was cutting off leading zeroes in the binary conversion
        temp = "0" + temp
    conv = conv + temp  # adds it to the conv string
#print(str(conv))  debug statement
#print(conv[0])  debug statement

length = len(conv)  # length of the binary message we want to send
#print(length)  debug statement
for k in range (0, length):  # looping through the binary message we want to send
    digit = conv[k]  # getting the digit to send
    x = 1  # setting up our while loop
    if turn == "White":  # we change the turn to the other color so we can print it out
        turn = "Black"
    elif turn == "Black":
        turn = "White"
    while x == 1 or x == None:  # this allows us to go again if we randomly chose an invalid move or a move that didn't fit our criteria, also it kept returning as None for some reason, so I just said that was an unsuccessful go too
        x = getmove(digit)  # we start the function that chooses and executes our move- if it returns a 1, we will do the whole thing over again

# to do list:
#   let the program detect when there is not a possible move and have it give a hit that there is not a possible move to send the specific digit
#       Would prevent any infinite loops (though I haven't had any yet)
#   Allow the game to check if there is a checkmate or check, and say something/restart if needed
#       This would make the game look more realistic 