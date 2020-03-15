"""
This script simulates a 2-player game of Connect-4 with both players being human.
Two players can input their respective movements.
"""

import numpy as np

class Board:
    def __init__(self,n):
        '''
        Initialize the board with a size of n
        '''
        self.board  = np.zeros((n,n))
        self.column_entry = np.zeros((n,1))
        self.n = n

    def display(self):
        '''
        To display the board
        '''
        b = self.board
        for col in b:
            colstr = [str(int(a)) for a in col]
            print("  ".join(colstr))
        print("The columns are numbered 1 to " + str(self.n) + ", left to right")

    def mark_board(self,player,column):
        '''
        To mark the player1 and player2 signs on the Board
        based on their entry
        '''
        column -= 1
        n = self.n
        if player == 1: mark = 1
        else: mark = 2
        i = int(self.column_entry[column].item())
        self.board[n-i-1,column] = mark
        self.column_entry[column] += 1

    def check_valid(self,column):
        '''
        check if the move is valid
        '''
        if column < 0 or column > self.n:
            print('\nInvalid column, out of grid')
            return False
        if self.board[0][column-1] != 0:
            print('\nColumn is full. Choose another column')
            return False
        return True

class Connect_Four:
    def __init__(self):
        self.player = 1
        self.finished = False
        self.n = int(input("\n Enter the dimension of the board (greater than 4) you want to play with: \n"))
        self.board = Board(self.n)
        self.board.display()

    def play(self):
        while self.finished == False:
            column = self.get_column()
            while not self.board.check_valid(column):
                column = self.get_column()
            self.board.mark_board(self.player,column)
            self.board.display()
            self.finished = self.checkfinished(self.board.board)
            if self.player == 1: self.player = 2
            else: self.player = 1

        if self.player == 1:
            print("\n Congratulations Player2!\n")
        else:
            print("\n Congratulations Player1! \n")

        playagain = input("\n Do you want to play again? y/n: \n")
        if playagain == "y":
            self.finished = False
            self.board = Board()
            self.play()
        else:
            print("\n Thank you for your time, have a good day! \n")

    def get_column(self):
        if self.player == 1:
            column = int(input("\n Player 1, plese enter the column number: \n"))
        else:
            column = int(input("\n Player 2, plese enter the column number: \n"))
        return column

    def checkfinished(self,board):
        n = self.n
        #row check, if 4 consecutive elements in a row are same
        for i in range(n-4+1):
            for j in range(n):
                if (board[i,j] == board[i+1,j] == board[i+2,j] == board[i+3,j]) and (board[i,j] in [1,2]):
                    print("1")
                    return True
        #column check, if 4 consecutive elements in a column are same
        for i in range(n-4+1):
            for j in range(n):
                if (board[j,i] == board[j,i+1] == board[j,i+2] == board[j,i+3]) and (board[j,i] in [1,2]):
                    print("2")
                    return True
        #main diagonal direction check
        for i in range(n-4+1):
            for j in range(n-4+1):
                if (board[i,j] == board[i+1,j+1]==board[i+2,j+2]==board[i+3,j+3]) and (board[i,j] in [1,2]):
                    print("3")
                    return True
        for i in range(3,n):
            for j in range(n-4+1):
                #print(i,j)
                if (board[i,j] == board[i-1,j+1]==board[i-2,j+2]==board[i-3,j+3]) and (board[i,j] in [1,2]):
                    print("4")
                    return True
        return False


if __name__=="__main__":
    game = Connect_Four()
    game.play()
