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
    """
    If line has many black and gray pixels
    loss get lesser

    :param y:
        np.ndarray, with dim - 1 and with [0,1] values
    :return:
        (-1) * sum of (1 - y[i])^2
    """
    return -np.sum(np.square(1 - y))


def dmse(y):
    """
    Dispersion mean squares error
    It just (n / (n - 1)) * linear_mean_squares
    This loss consider length of vector
    """
    return (len(y) / (len(y) - 1)) * linear_mean_squares(y)