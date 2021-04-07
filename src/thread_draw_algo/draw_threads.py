from math import sin, cos, radians
from src.thread_draw_algo.thread import *
from heapq import nsmallest
import random


def pre_count_xy(points, radius):
    """
        Pre-count coords for circle points
    """
    points_coord = []
    for i in range(points):
        rad = radians(-90 + i * 360 / points)
        x = round(radius + radius * sin(rad))
        y = round(radius + radius * cos(rad))
        points_coord.append((x, y))
    return points_coord


def draw(pixels, top=1, points=600, radius=500, max_iter=75, ignore=60):
    """
    On each iteration takes `sqrt(points) + 1` points randomly
    and tries to find `top`-best threads for this point on current picture.
    After this need to write all found threads.

    :param top:
        Number of thread with the smallest weight, which takes
        from one random point
    :param ignore
        How much of the points to ignore when drawing threads
    :return:
        List of pairs of threads' points
    """
    eps = points // ignore  # how many points we ignore around our point
    all_threads = list()
    xy_container = pre_count_xy(points, radius)
    for k in range(max_iter):
        k_threads = list()
        print(f'Start iteration {k}')
        for _ in range(round(points ** (1 / 2)) + 1):
            i = random.randint(0, points - 1)
            threads = [
                Thread(i, j % points,
                       xy_container[i], xy_container[j % points],
                       pixels)
                for j in range(i + eps, i + points - eps)
            ]
            threads = nsmallest(top, threads, key=lambda x: x.weight)
            k_threads += threads
        for thread in k_threads:
            thread.purge_weight(pixels)
        all_threads += k_threads
    return map(str, all_threads)
