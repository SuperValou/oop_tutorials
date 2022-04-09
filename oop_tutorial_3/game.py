class CellSymbol(object):
    BLANK = "[ ]"
    X_SYMBOL = "[x]"
    O_SYMBOL = "[o]"


class TicTacToeGame(object):
    """
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
        self._player_one = player_one
        self._player_two = player_two
        for i in range(0, 8):
            self._grid[i] = CellSymbol.BLANK
        self._current_player = player_one

    def play_move(self, grid_cell_index):
        # TODO: put the symbol of the current player at the given cell index
        if grid_cell_index < 0 or grid_cell_index > len(self._grid):
            raise ValueError("grid_cell is out of range")

        cell_symbol = self._grid[grid_cell_index]
        if cell_symbol != CellSymbol.BLANK:
            raise ValueError("This cell is already occupied by a {symbol}"
                             .format(symbol=cell_symbol))

        symbol = self.get_player_symbol(self._current_player)
        self._grid[grid_cell_index] = symbol

    def swap_player(self):
        # TODO: change the current player
        if self._current_player == self._player_one:
            self._current_player = self._player_two
        else:
            self._current_player = self._player_one

    def get_player_symbol(self, player):
        # TODO: return the CellSymbol corresponding to 'player'
        if player == self._player_one:
            return CellSymbol.X_SYMBOL
        return CellSymbol.O_SYMBOL

    def is_filled(self):
        # TODO: return whether or not the grid is full
        for i in range(0, 8):
            if self._grid[i] == CellSymbol.BLANK:
                return False
        return True

    def is_won_by(self, player):
        # TODO: return whether or not the given player won the game
        symbol = self.get_player_symbol(player)

        won_horizontal = (False
            or (self._grid[0] == symbol and self._grid[1] == symbol and self._grid[2] == symbol)
            or (self._grid[3] == symbol and self._grid[4] == symbol and self._grid[5] == symbol)
            or (self._grid[6] == symbol and self._grid[7] == symbol and self._grid[8] == symbol)
        )

        won_vertical = (False
            or (self._grid[0] == symbol and self._grid[3] == symbol and self._grid[6] == symbol)
            or (self._grid[1] == symbol and self._grid[4] == symbol and self._grid[7] == symbol)
            or (self._grid[2] == symbol and self._grid[5] == symbol and self._grid[8] == symbol)
        )

        won_diag = (False
           or (self._grid[0] == symbol and self._grid[4] == symbol and self._grid[8] == symbol)
           or (self._grid[6] == symbol and self._grid[4] == symbol and self._grid[2] == symbol)
        )

        return won_horizontal or won_vertical or won_diag

