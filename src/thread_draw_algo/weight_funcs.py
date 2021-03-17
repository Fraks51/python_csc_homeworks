import numpy as np


def linear_mean_squares(y):
    """
    find loss for linear y
    :param y:
        np.ndarray, with dim - 1 and with [0,1] values
    :return:
        np.float ||x - y||^2 we assume, that
        all x is equal 0, because our line full black
    """
    return np.mean(np.square(y))


def black_collector(y):
    return -np.sum(np.square(1 - y))


def dmse(y):
    return (len(y) / (len(y) - 1)) * linear_mean_squares(y)