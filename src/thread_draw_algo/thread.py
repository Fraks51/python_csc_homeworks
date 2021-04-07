import numpy as np
from math import ceil


class Thread:
    """
    Class for painting thread
    """
    def __init__(self, i, j, coord_i, coord_j, pixels):
        self.i = i
        self.j = j
        self.coord_i = coord_i
        self.coord_j = coord_j
        self.pixels = pixels
        self.weight = self._find_weight()

    def _get_linspace(self):
        x_i, y_i = self.coord_i
        x_j, y_j = self.coord_j
        steps = ceil(np.linalg.norm([x_j - x_i, y_j - y_i]))
        xs = (np.linspace(x_i, x_j, num=steps) % len(self.pixels)).astype(int)
        ys = (np.linspace(y_i, y_j, num=steps) % len(self.pixels)).astype(int)
        return steps, xs, ys

    def _find_weight(self):
        """
        :return:
            weight for this thread counting by mse
        """
        steps, x, y = self._get_linspace()
        ys = np.array([self.pixels[x[i]][y[i]] for i in range(steps)])
        return np.mean(np.square((np.array(ys))))

    def purge_weight(self, pixels):
        """
        Draw this thread
        Make all pixels on the thread's way - white (1)
        """
        steps, x, y = self._get_linspace()
        for i in range(steps):
            pixels[x[i]][y[i]] = 1

    def __str__(self):
        return f"{self.i} {self.j}"


