class TictactoeException(Exception): #declare class that inherits from Exception
    def __init__(self, message):
        self.message = message #store an instance variable called message
        super().__init__(message)

class Board():
    valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"] #create class variable

    def __init__(self): #init function with only the self argument
        self.board_array = [[" ", " ", " "] for _ in range(3)] #create a list of empty lists (3x3)
        self.turn = "X"

    def __str__(self): #string method to display board
        lines = [] #empty board
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n") #top row
        lines.append("-----------\n") #separation line
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n") #middle row
        lines.append("-----------\n") #separation line
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n") #bottom row
        board = "".join(lines)
        return board
    
    def move(self, move_string):
        if move_string.lower() not in Board.valid_moves: #if the move isn't valid
            raise TictactoeException("That's not a valid move. Please try again.") #display error
        
        move_index = Board.valid_moves.index(move_string.lower()) #index num of the location in the string of valid moves
        row = move_index // 3 #get row number using floor division
        column = move_index % 3 #get column number using remainder
        
        if self.board_array[row][column] != " ": #if that spot on the board is already filled in with an X or O
            raise TictactoeException("That spot is taken. Please try again.") #display error
        
        self.board_array[row][column] = self.turn #fill in the spot with an X or an O

        if self.turn == "X":
            self.turn = "O" #switch to O if X just played
        else:
            self.turn = "X" #switch to X if O just played
    
    def whats_next(self):
        cat = True 
        for i in range(3): #iterate over the rows
            for j in range(3): #iterate over the columns
                if self.board_array[i][j] == " ":
                    cat = False #if there's still an empty space, keep playing
                else:
                    continue
                break
            else:
                continue
            break #if all columns and rows are filled, move to the next section of the code
        if (cat):
            return (True, "Cat's Game. Nobody won. Meow.")
        win = False #win will be marked false until every possibility has been checked
        for i in range(3): # check rows
            if self.board_array[i][0] != " ": #if the spot is filled
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]: #if all spots in that row have the same player
                    win = True #change win status to true
                    break #that player has won so move on to the next section
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]: #if all spots in that column have the same player
                        win = True #change win status to true
                        break #that player has won so move on to the next section
        if not win:
            if self.board_array[1][1] != " ": # check diagonals
                if self.board_array[0][0] ==  self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        if not win: #if there are still empty spaces
            if self.turn == "X": 
                return (False, "X's turn.") #check whose turn it was and keep playing, switching to the other player
            else:
                return (False, "O's turn.")
        else:
            if self.turn == "O": #check who just went and let them know they won
                return (True, "X wins!")
            else:
                return (True, "O wins!")
            

#create new instance of Board
board = Board()

#define function to play the game
def play_tictactoe():
    welcome_message = f"Welcome to TicTacToe! \n Player X goes first. You can play any of the following moves: {Board.valid_moves}. \n {board}"
    print(welcome_message)

    game_over = False


    while not game_over: #as long as the game keeps going
        try:
            move_string = input("What move would you like to play?") #define input variable
            board.move(move_string) #input their move into the move function
            print(board) #print updated board
            
            game_over, message = board.whats_next()
            print(message)

        except TictactoeException as e:
            print(f"An error occured: {e.message}")
            continue #keep playing

#call the play function
play_tictactoe()