import os
#!this method help me to clear screen for better coding
def clearscreen():
    os.system("cls")
class player:
    def __init__(self):
        self.name=""
        self.symbol=""
    def cname(self):
        print("Enter your name")
        while True:
            #! input in the loop to avoid infinite loop that will happen because their is no end condition if the name is incorrect
            name=input()
            self.name=name
            if  not self.name.isalpha():
                print("Name must be only letters,try again")
            else:
                # print("correct")
                break
    def csymbol(self):
        print(f"{self.name.capitalize()} Choose (X-O)")
        while True:
            print("X or O")
            ch=input()
            self.symbol=ch.upper()
            if len(self.symbol)>1 or (self.symbol != "x".upper() and self.symbol != "o".upper()):
                print("Error\nyou must choose only X or O\ntry again")
            else:
                break
class menu:
    def main_menu(self):
        print("Welcome to Tic-Tac-Toe")
        print("1-Start game\n2-Quit game")
        ch=int(input())
        return ch
    def end_game_menu(self):
        print("Game over!")
        print("1-Restart game\n2-Quit game")
        ch=int(input())
        return ch
class board:
    def __init__(self):
        #! --str(i)--  so we can use join to display the board
        self.board=[str(i) for i in range(1,10)]
    def board_display(self):
        #* this to make 3 raws
        for i in range(0,9,3):
            # * this will work on the index
            print("|".join(self.board[i:i+3]))
            if i<6:
                print("-----")
    def update_board(self,choice,symbol):
        # true or false
        if self.is_valid(choice):
            self.board[choice-1]=symbol
            return True
        else :
            print("not valid position")
            return False

    
    def is_valid(self,position):
        if self.board[position-1]=='X' or self.board[position-1]=='O':
            return False
        return True
    def reset(self):
        # for i in range(9):
            # self.board[i]=str(i+1)
        #! this is better than use for loop
        self.board=[str(i) for i in range(1,10)]
class game:
    def __init__(self):
        #! this objects only life in game class
        #* players is a list so we need to treat it like a list
        #*the player 1 who is in index 0 in self.player and player 2 who is in index 1 in self.player
        self.player=[player(),player()]
        self.board=board()
        self.menu=menu()
        self.cplayer=0
    def startgame(self):
        clearscreen()
        ch=self.menu.main_menu()
        first=0
        if ch ==1 :
            #the name and symbol 
            #! enumerate for indexing 
            for index,i in enumerate(self.player,1):
                print(f"Player {index}, Enter your name:")
                i.cname()
                # to give the second player his symbol automatically
                if first==0:
                    i.csymbol()
                first=1
                clearscreen()
            self.player[1].symbol='O' if self.player[0].symbol=='X' else 'X'
            self.play()
        else:
            self.quit()

    def play(self):
        
        while True:
            turn = self.player[self.cplayer]
            self.board.board_display()
            print(f"{turn.name.capitalize()}'s turn\nEnter position")
            #this is to make attempts for incorrect inputs
            attempt = 3
            valid_move = False
            
            while attempt > 0:
                try:
                    pos = int(input())
                    if self.board.update_board(pos, turn.symbol):
                        valid_move = True
                        # out from input
                        break
                    else:
                        attempt -= 1
                        clearscreen()
                        self.board.board_display()
                        print(f"Position already taken. Attempts left: {attempt}")
                except:
                    attempt -= 1
                    print(f"Invalid input. Please enter a number from 1 to 9. Attempts left: {attempt}")
            if valid_move==False:
                self.restart()

            if self.win():
                clearscreen()
                self.board.board_display()
                print(f"{turn.name.capitalize()} wins! 🎉")
                if self.menu.end_game_menu() == 1:
                    self.restart()
                else:
                    self.quit()

            if self.draw():
                clearscreen()
                self.board.board_display()
                print("Draw! No one wins.")
                if self.menu.end_game_menu() == 1:
                    self.restart()
                else:
                    self.quit()

            self.switch()
            clearscreen()

        
    def win(self):
        b=self.board.board
        playturn=self.player[self.cplayer]
        #* 0 2 5 8
        for i in range(0,9,3):
            if b[i]==b[i+1]==b[i+2] == playturn.symbol:
                return True
            #* 0 1 2
        for i in range(3):
            if b[i]==b[i+3]==b[i+6]==playturn.symbol:
                return True
        if b[0]==b[4]==b[8]==playturn.symbol:
            return True
        if b[2]==b[4]==b[6]==playturn.symbol:
            return True
        
        #! to let the fun check all raws
        return False
    def draw(self):
        if self.win()==False and all(cell in['X','O'] for cell in self.board.board):
            return True
        return False
    def quit(self):
        print("Good bye")
        exit()
    def restart(self):
        clearscreen()
        print("--Game restarted--")
        self.board.reset()
        self.play()
    def switch(self):
        if self.cplayer==0:
            self.cplayer=1
        else:
            self.cplayer=0
g=game()
g.startgame()
