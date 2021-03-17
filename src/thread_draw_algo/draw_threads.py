from src.thread_draw_algo.weight_funcs import *
from math import sin, cos, radians
from src.thread_draw_algo.thread import *
import random


def count_xy(points, radius, index):
    """
    Count coords for circle points
    """
    rad = radians(-90 + index * 360 / points)
    x = round(radius + radius * sin(rad))
    y = round(radius + radius * cos(rad))
    return x, y


def change_pic(pixels, threads):
    """

    :param pixels:
        Current image
    :param threads:
        List of threads to draw
    """
    for thread in threads:
        thread.purge_weight(pixels)


def draw(pixels, weight_func=linear_mean_squares, top=1, points=600, radius=500, max_iter=78):
    """

    :param pixels:
        Image 2-D array
    :param weight_func:
        Function for find loss between 2 vectors
        Takes from src.thread_draw_algo.weight_funcs
    :param top:
        Number of thread with the smallest weight, which takes
        from one random point
    :param points:
        Number of points on the draw circle
    :param radius:
        Circle radius
    :param max_iter:
        Number of iterations
    :return:
        List of pairs of threads' points
    """
    eps = points // 60  # how many points we ignore around our point
    all_threads = list()
    for k in range(max_iter):
        k_threads = list()
        print(f'Start iteration {k}')
        for _ in range(round(points ** (1 / 2)) + 1):
            threads = list()
            i = random.randint(0, points)
            for j in range(points):
                if abs(i - j) > eps and abs(points - (i - j)) > eps:
                    coord_i = count_xy(points, radius, i)
                    coord_j = count_xy(points, radius, j)
                    threads.append(Thread(i, j, coord_i, coord_j, pixels, weight_func))
            threads.sort()
            threads = threads[:top]
            k_threads += threads
        change_pic(pixels, k_threads)
        all_threads += k_threads
    return map(lambda x: x.to_pair(), all_threads)
