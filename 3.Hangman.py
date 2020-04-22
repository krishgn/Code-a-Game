'''
Here I implement the game of Hangman. The words that can be tested are initialized in a list as global variable.
This can be modified by the user.
'''

from random import randint
wordlist = ["insight","artificial","intelligence","machine","learning", \
            "silicon","management","program",'clustering', 'regression', 'likelihood']
listlen = len(wordlist)

class Word:
    def __init__(self):
        '''
        Initializing the word class
        '''
        val = randint(0, listlen-1)
        self.word = wordlist[val]
        self.charlist = list(self.word)
        wordlen = len(self.charlist)
        self.anslist = ["-"]*wordlen
        print(self.anslist)
        self.wrongguess = 0
        self.wronglist = []

    def checkchar(self,char):
        if char in self.charlist:
            charindex = [i for i in range(len(self.charlist)) if self.charlist[i] == char]
            for i in charindex:
                self.anslist[i] = char
            print(self.anslist)
        else:
            print("That's a wrong guess.")
            if char in self.wronglist:
                print("You have tried this before. Enter another letter.")
                print("You have " + str(6-self.wrongguess) + " guesses remainig")
            else:
                self.wrongguess +=1
                self.wronglist.append(char)
                print("You have " + str(6-self.wrongguess) + " guesses remainig")
            self.display(self.wrongguess)
        return self.wrongguess, self.anslist

    def display(self,wrongguess):
        if wrongguess == 1:
            print("_________")
            print("|     |")
            print("|	 O")
            print("|")
            print("|")
            print("|")
            print("|________")
        elif wrongguess == 2:
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	 |")
            print("|	 |")
            print("|")
            print("|________")
        elif wrongguess == 3:
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|")
            print("|	 |")
            print("|")
            print("|________")
        elif wrongguess == 4:
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|/")
            print("|	 |")
            print("|")
            print("|________")
        elif wrongguess == 5:
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|/")
            print("|	 |")
            print("|	/ ")
            print("|________")
        elif wrongguess == 6:
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|/")
            print("|	 |")
            print("|	/ \ ")
            print("|________")

class Hangman:
    def __init__(self):
        self.word = Word()
        self.finished = False

    def play(self):
        while self.finished == False:
            char = input("Enter a character: \n")
            wrongguess, anslist = self.word.checkchar(char)
            self.finished = self.checkfinished(wrongguess, anslist)
        choice = input("Do you want to play again? y/n: \n")
        if choice == "y":
            game = Hangman()
            game.play()
        else:
            print("Thank you for your time, have a good day!")

    def checkfinished(self,wrongguess,anslist):
        if wrongguess == 6:
            print('Game Over!')
            return True
        if "-" not in anslist:
            print("Congratulations!")
            return True
        return False

if __name__ == "__main__":
    game = Hangman()
    game.play()
