import os
from game import TicTacToeGame
from ui import TicTacToeUi


def main():
    print("Hello {name}".format(name=os.getlogin()))

    game = TicTacToeGame()
    ui = TicTacToeUi(game)
    ui.show()





if __name__ == '__main__':
    main()
