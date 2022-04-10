from game import CellSymbol


class UserInterface(object):
    def __init__(self, game):
        self._game = game

    def show(self):
        print("Welcome!")
        player_1 = input("Please enter Player 1 name:\n") or "Player 1"
        player_2 = input("Please enter Player 2 name:\n") or "Player 2"

        self._game.initialize(player_1, player_2)

        while True:
            # display the board in the console
            self._show_board()

            # get the player input
            player_input = input("{player}, your turn!\n"
                                 "(type the cell index you want to fill, or 'quit' to stop.)\n"
                                 .format(player=self._game.current_player))

            # check if player want to stop the game
            if player_input.lower() == 'stop' or player_input.lower() == 'quit':
                break

            # convert the player input to an int
            try:
                cell_index = int(player_input)
            except (TypeError, ValueError):
                print("Incorrect input '{player_input}'.".format(player_input=player_input))
                continue

            # play the move
            # TODO: play the move with 'cell_index'

            # check if the game is won by the current player
            # TODO: check if the game is won by the current player

            # check if the game can still be played
            # TODO: check if the game can still be played

            # swap player
            # TODO: change player

        self._show_board()
        self._display_game_over()

    def _show_board(self):
        board = ""\
            "__________________\n"\
            "|     |     |     |\n"\
            "|  {0}  |  {1}  |  {2}  |\n"\
            "|_____|_____|_____|\n"\
            "|     |     |     |\n"\
            "|  {3}  |  {4}  |  {5}  |\n"\
            "|_____|_____|_____|\n"\
            "|     |     |     |\n"\
            "|  {6}  |  {7}  |  {8}  |\n"\
            "|_____|_____|_____|\n"

        board_symbols = [self._get_drawing(symbol) for symbol in self._game.grid]
        board = board.format(*board_symbols)
        print(board)

    def _get_drawing(self, symbol):
        if symbol == CellSymbol.BLANK:
            return " "
        if symbol == CellSymbol.O_SYMBOL:
            return "O"
        if symbol == CellSymbol.X_SYMBOL:
            return "X"
        raise ValueError("{symbol} is not a symbol".format(symbol=symbol))

    def _display_game_over(self):
        # TODO: congratulate the winner, or tell the players that the game is a tie
        pass
