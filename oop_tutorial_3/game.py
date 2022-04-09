class CellSymbol(object):
    BLANK = "[ ]"
    X_SYMBOL = "[x]"
    O_SYMBOL = "[o]"


class TicTacToeGame(object):
    """
    GRID INDEX:
 __________________
|     |     |     |
|  0  |  1  |  2  |
|_____|_____|_____|
|     |     |     |
|  3  |  4  |  5  |
|_____|_____|_____|
|     |     |     |
|  6  |  7  |  8  |
|_____|_____|_____|
    """

    def __init__(self):
        self._grid = [CellSymbol.BLANK, CellSymbol.BLANK, CellSymbol.BLANK,
                      CellSymbol.BLANK, CellSymbol.BLANK, CellSymbol.BLANK,
                      CellSymbol.BLANK, CellSymbol.BLANK, CellSymbol.BLANK]

        self._player_one = None
        self._player_two = None

        self._current_player = None

    @property
    def grid(self):
        return self._grid

    @property
    def current_player(self):
        return self._current_player

    def initialize(self, player_one, player_two):
        # TODO: initialize player-related fields
        pass

    def play_move(self, grid_cell_index):
        # TODO: put the symbol of the current player at the given cell index
        pass

    def swap_player(self):
        # TODO: change the current player
        pass

    def is_filled(self):
        # TODO: return whether or not the grid is full
        return False

    def is_won_by(self, player):
        # TODO: return whether or not the given player won the game
        return False

    def _get_player_symbol(self, player):
        # TODO: return the CellSymbol corresponding to 'player'
        return CellSymbol.BLANK
