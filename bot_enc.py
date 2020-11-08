import chess
from random import *  # idk why I can't just import random, but that didn't work so I use the from and * format

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

board = chess.Board()
turn = "Black"
retarr = ["start"]  # this is a variable to store the moves we all do as an array so we can return them all to the discord bot later

def getmove(digit):
    store = randomletter()
    store = store + randomnumber()
    second = randomletter()
    second = second + randomnumber()

    if second == "a1":
        if str(a1) != digit:
            return 1
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

    if store == second:
        return 1

    first = store
    store = store + second
    x = makemove(store)
    if x == 1:
        return 1
    elif x == 0:
        if turn == "White":
            send = "White: "  # don't need to print this stuff, just need to send it- removed a bunch of print statements
        elif turn == "Black":
            send = "Black: "
        send = send + "Move "
        send = send + first
        send = send + " to "
        send = send + second
        retarr.append(send)  # instead of sending this over the network, we return it to the discord bot
        return 0

def randomletter():
    x = randint(0, 7)
    y = ""

    if x == 0:
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

    return y

def randomnumber():
    x = randint(1,8)
    return str(x)

def makemove(store):
    move = chess.Move.from_uci(store)
    x = move in board.legal_moves
    if x == True:
        board.push(move)  # executes the move we don't need to print it this time- yay I guess
        return 0
    elif x == False:
        return 1

def messagesend(uword):  # the function that the bot calls
    # honestly I have no idea why I have to declare turn here but don't have to for none of the other global variables
    # also- see the enc code I wrote for comments, I'm only commenting on what I change from that here
    # since I literally just stole my own code and made it work for a discord bot
    global turn
    turn = "Black"
    retarr.clear()

    conv = ""
    length = len(uword)  # grabbing the length of the message for later- we get the message from the discord bot
    for x in range (0, length):
        temp = ''.join(format(i, 'b') for i in bytearray(uword[x], encoding ='utf-8'))
        if len(temp) == 7:
            temp = "0" + temp
        conv = conv + temp
    length = len(conv)
    for k in range (0, length):
        digit = conv[k]
        x = 1
        if turn == "White":
            turn = "Black"
        elif turn == "Black":
            turn = "White"
        while x == 1 or x == None:
            x = getmove(digit)

    return retarr  # returns the array of moves that we made