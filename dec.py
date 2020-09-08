import binascii

def getmove(move):  # function to tell if a move is a 1 or a 0
    amount = len(move)  # we find the length of the move so we can access the last two characters in the string which is the space we care abou
    space = move[amount - 2]
    space = space + move[amount - 1]

    # might be a better way to do this, but I can't think of this right now so it'll work
    if space == "a1":  # we check to see if the space is a specific space on the check board
        return 1  # we return if it's a 1 or a 0
    elif space == "b1":
        return 0
    elif space == "c1":
        return 1
    elif space == "d1":
        return 0
    elif space == "e1":
        return 1
    elif space == "f1":
        return 0
    elif space == "g1":
        return 1
    elif space == "h1":
        return 0
    elif space == "a2":
        return 0
    elif space == "b2":
        return 1
    elif space == "c2":
        return 0
    elif space == "d2":
        return 1
    elif space == "e2":
        return 0
    elif space == "f2":
        return 1
    elif space == "g2":
        return 0
    elif space == "h2":
        return 1
    elif space == "a3":
        return 1
    elif space == "b3":
        return 0
    elif space == "c3":
        return 1
    elif space == "d3":
        return 0
    elif space == "e3":
        return 1
    elif space == "f3":
        return 0
    elif space == "g3":
        return 1
    elif space == "h3":
        return 0
    elif space == "a4":
        return 0
    elif space == "b4":
        return 1
    elif space == "c4":
        return 0
    elif space == "d4":
        return 1
    elif space == "e4":
        return 0
    elif space == "f4":
        return 1
    elif space == "g4":
        return 0
    elif space == "h4":
        return 1
    elif space == "a5":
        return 1
    elif space == "b5":
        return 0
    elif space == "c5":
        return 1
    elif space == "d5":
        return 0
    elif space == "e5":
        return 1
    elif space == "f5":
        return 0
    elif space == "g5":
        return 1
    elif space == "h5":
        return 0
    elif space == "a6":
        return 0
    elif space == "b6":
        return 1
    elif space == "c6":
        return 0
    elif space == "d6":
        return 1
    elif space == "e6":
        return 0
    elif space == "f6":
        return 1
    elif space == "g6":
        return 0
    elif space == "h6":
        return 1
    elif space == "a7":
        return 1
    elif space == "b7":
        return 0
    elif space == "c7":
        return 1
    elif space == "d7":
        return 0
    elif space == "e7":
        return 1
    elif space == "f7":
        return 0
    elif space == "g7":
        return 1
    elif space == "h7":
        return 0
    elif space == "a8":
        return 0
    elif space == "b8":
        return 1
    elif space == "c8":
        return 0
    elif space == "d8":
        return 1
    elif space == "e8":
        return 0
    elif space == "f8":
        return 1
    elif space == "g8":
        return 0
    elif space == "h8":
        return 1


go = input("Do you want to translate a chess move? (y/n)")  # sets up the loop even though they want to if they start up the program
message = []  # dynamic array which we will use later
while go == "y":  # loops while the user wants to translate the move
    move = input("What is the chess move in question?")  # stores the move the user wants to check
    x = getmove(move)  # finds out if a 1 or a 0
    message.append(x)  # puts it at the back of the array
    go = input("Do you want to continue to translate chess moves? (y/n)")  # do you want to continue

length = len(message)  # the number of bits that were transferred
print("The message is:", end = " ")
for x in range (0, length):  # will print out every bit that was decoded
    print(message[x], end = " ")
print()

# to do:
#   Maybe make it so it will decode messages not in the same format that I encode them in
#       idk how to do that yet though
#   Do the translation from binary data to ascii text in the program
#       Would be easier for the user, but more work for me :(