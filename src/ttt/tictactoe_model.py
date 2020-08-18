import numpy as np

class TicTacToeModel:

    def __init__(self, w, h, win_size):
        self.win_size = win_size
        self.w = w
        self.h = h
        self.fields = np.zeros((h, w))

        self.player = 1

    # act by current player and change player
    # return game_state or -1 (the field is occupied)
    def act(self, x, y):
        if self.fields[y, x] == 0:
            self.fields[y, x] = self.player
            result = self.game_state()
            self.player = 2 if self.player == 1 else 1
            return result
        else:
            return -1

    """
        0 - continue
        1,2 - player won
        3 - draw
    """
    def game_state(self):
        if self.check_win():
            return self.player
        elif self.check_draw():
            return 3
        else:
            return 0

    def reset(self):
        self.fields = np.zeros(np.shape(self.fields))

    def check_win(self):
        def check_seq(x_start, y_start, dx, dy):
            fields = self.fields
            win_size = self.win_size
            (h, w) = np.shape(self.fields)

            x_end = x_start + dx * (win_size - 1)
            y_end = y_start + dy * (win_size - 1)

            if 0 <= x_end < w and 0 <= y_end < h:
                val = fields[y_start, x_start]
                if val == 0:
                    return False

                (x, y) = (x_start + dx, y_start + dy)
                while x - x_start < win_size and y - y_start < win_size:
                    if val != fields[y, x]:
                        return False
                    x += dx
                    y += dy
                return True
            else:
                return False

        (h, w) = np.shape(self.fields)
        fields = self.fields

        for x in range(w):
            for y in range(h):
                if check_seq(x, y, 0, 1) \
                        or check_seq(x, y, 1, 0) \
                        or check_seq(x, y, -1, 1) \
                        or check_seq(x, y, 1, 1):
                    return fields[y, x]
        return 0

    def check_draw(self):
        return 0 not in self.fields
