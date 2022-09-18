board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
def steps(step,symbol):
    ind = board.index(step)
    board[ind] = symbol

def result():
    win = "" 
    for i in victories:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = "O"                
    return win

end_game = False
first = True
 
while end_game == False:
 
    draw_board(board)
    if first == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))
 
    steps(step,symbol)
    win = result()
    if win != "":
        end_game = True
    else:
        end_game = False
    first = not(first)

    draw_board(board)
print("Победил", win)

