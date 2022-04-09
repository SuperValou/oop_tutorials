from game import TicTacToeGame
from ui import UserInterface


def main():
    game = TicTacToeGame()
    ui = UserInterface(game)
    ui.show()


if __name__ == '__main__':
    main()
