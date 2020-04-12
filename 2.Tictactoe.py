"""
This script simulates a 2-player game of Tictactoe with both players being human.
Two players can input their respective movements.
The board is 3x3
"""

class Board:
    #initializes the Board class
    def __init__(self):
        self.board = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    def display(self):
        # displays the board in 3x3 format
        for i in range(3):
            print('   '.join(self.board[i*3 : i*3 + 3]))

    def mark_board(self, player, move):
        # marks the board with X or 0 depending on the player status
        if player == 1:
            self.board[move] = 'X'
        else:
            self.board[move] = 'O'

class Tictactoe:
    def __init__(self):
        # initializes the game class
        self.finished = False
        self.player = 0
        self.board = Board()

    def get_move(self):
        #asks move from the player and marks it if not already marked
        self.board.display()
        if self.player == 0:
            move_index = input("Player 1 can now enter his/her move: \n")
        else:
            move_index = input("Player 2 can now enter his/her move: \n")
        move_dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8}
        move = move_dict[move_index]
        if self.board.board[move] == 'X' or self.board.board[move] == 'O':
            print('\n That position is taken. Try another \n')
            self.get_move()
        else:
            self.board.mark_board(self.player,move)

    def play(self):
        while self.finished == False:
            self.get_move()
            self.finished = self.checkfinished(self.board.board)
            self.player = not self.player
        self.board.display()
        if self.player == 0:
            print("\n Congratulations player 1 \n")
        else:
            print("\n Congratulations player 0 \n")
        playagain = input("\n Do you want to play again? y/n: \n")
        if playagain == "y":
            self.finished = False
            self.board = Board()
            self.play()
        else:
            print("\n Thank you for your time, have a good day! \n")

    def checkfinished(self,board):
        # check if the game is complete after each move
        if (board[0] == board[1] == board[2]): return True
        if (board[3] == board[4] == board[5]) : return True
        if (board[6] == board[7] == board[8]): return True
        if (board[0] == board[3] == board[6]): return True
        if (board[1] == board[4] == board[7]): return True
        if (board[2] == board[5] == board[8]): return True
        if (board[0] == board[4] == board[8]): return True
        if (board[2] == board[4] == board[6]) : return True
        return False

if __name__ == "__main__":
    game = Tictactoe()
    game.play()
