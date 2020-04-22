from random import randint
wordlist = ["insight","artificial","intelligence","machine","learning", \
            "silicon","management","program"]
listlen = len(wordlist)

class Word:
    def __init__(self):
        val = randint(0, listlen-1)
        self.word = wordlist[val]
        self.charlist = list(self.word)
        wordlen = len(self.charlist)
        self.anslist = ["-"]*wordlen
        print(self.anslist)
        self.wrongguess = 0
        self.wronglist = []
        self.image = Picture()

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
            self.image.display(self.wrongguess)
        return self.wrongguess, self.anslist

class Picture:
    def __init__self():
        self.symbols = ['0','|','/','\\','/','\\']

    def display(self,wrongguess):
        if wrongguess == 1:
            print('0')
        elif wrongguess == 2:
            print(' 0')
            print(' |')
        elif wrongguess == 3:
            print(' 0')
            print('/|')
        elif wrongguess == 4:
            print(' 0')
            print('/|\\')
        elif wrongguess == 4:
            print(' 0')
            print('/|\\')
            print('/')
        elif wrongguess == 5:
            print(' 0')
            print('/|\\')
            print('/\\')


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
