import discord
import chess
import bot_enc as enc

client = discord.Client()
board = chess.Board()

@client.event
async def on_ready():
    try:
        print('Logged in as {0.user}'.format(client))
    except:
        print("Could not login")

@client.event
async def on_message(message):
    if message.author == client.user:  # so we don't respond to our own messages- we shouldn't but just in case
        return
    if message.content.startswith("!hello"):
        await message.channel.send("world")
    elif message.content.startswith('!help'):  # if someone wants to list our functions
        await message.channel.send('!hello for a greeting and !board to print the current board')
        await message.channel.send('!check to check for the end of the game, and to reset the board if game is over')
        await message.channel.send('!move to send a move, must be in uci format and typed like: !move a2a3, for example')
    elif message.content.startswith('!board'):  # if someone wants to print the board
        await message.channel.send(board)
    elif message.content.startswith('!move'):  # if someone wants to make a move
        movestr = message.content
        movestr = movestr.replace("!move", "")
        movestr = movestr.strip()
        move = chess.Move.from_uci(movestr)
        board.push(move)
        await message.channel.send(board)
    elif message.content.startswith('!check'):  # if someone wants to check if the game is over
        x = board.is_checkmate()
        print(x)
        if x == True:
            await message.channel.send("Game Over due to checkmate!!")
            board.reset_board()
        x = board.is_stalemate()
        print(x)
        if x == True:
            await message.channel.send("Game Over due to stalemate...")
            board.reset_board()
    elif message.content.startswith('!send'):  # if someone wants to send a message
        uword = message.content
        uword = uword.replace("!send", "")
        uword = uword.strip()
        await message.channel.send(enc.messagesend(uword))
        
      
client.run('NzY1Nzc2NjM1MDg0ODAwMDIw.X4ZvEQ.YkLmObRSNdHnEmVJ2Ati9pPacSE')