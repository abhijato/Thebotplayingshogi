from chess import polyglot
from chess import variant
import chess
board = variant.GiveawayBoard()
while not board.is_game_over():
    with chess.polyglot.open_reader("bookchen.bin") as reader:
        moves=[]
        weight=[]
        for entry in reader.find_all(board):
            moves.append(entry.move)
            weight.append(entry.weight)
            print(entry)
    if len(weight)==0:
        break
    else:
        board.push(moves[weight.index(max(weight))])
    print("")
print(board)
