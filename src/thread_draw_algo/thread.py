import numpy as np


class Thread:
    def __init__(self, i, j, coord_i, coord_j, pixels, weight_func):
        self.i = i
        self.j = j
        self.pixels = pixels
        self.coord_i = coord_i
        self.coord_j = coord_j
        self.weight = self._find_weight(coord_i, coord_j, weight_func)

    def re_weight(self, pixels, weight_func):
        self.pixels = pixels
        self.weight = self._find_weight(self.coord_i, self.coord_j, weight_func)

    def cast_round(self, x):
        x = round(x)
        if x >= len(self.pixels):
            x -= 1
        elif x < 0:
            x = 0
        return x

    def _find_weight(self, coord_i, coord_j, weight_func):
        x_i, y_i = coord_i
        x_j, y_j = coord_j
        steps = abs(x_j - x_i) + abs(y_i - y_j)
        ys = list()
        last_x = -100
        last_y = -100
        for i in range(steps + 1):
            x = self.cast_round(x_i + (x_j - x_i) * (i / steps))
            y = self.cast_round(y_i + (y_j - y_i) * (i / steps))
            if not (x == last_x and y == last_y):
                last_x, last_y = x, y
                ys.append(self.pixels[x][y])
        return weight_func(np.array(ys))

    def purge_weight(self, pixels):
        x_i, y_i = self.coord_i
        x_j, y_j = self.coord_j
        steps = abs(x_j - x_i) + abs(y_i - y_j)
        last_x = -100
        last_y = -100
        for i in range(steps + 1):
            x = self.cast_round(x_i + (x_j - x_i) * (i / steps))
            y = self.cast_round(y_i + (y_j - y_i) * (i / steps))
            if not (x == last_x and y == last_y):
                last_x, last_y = x, y
                pixels[x][y] = 1

    def to_pair(self):
        return self.i, self.j

    def __lt__(self, other):
        return self.weight < other.weight


