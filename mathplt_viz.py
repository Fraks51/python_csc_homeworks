import matplotlib.pyplot as plt
from math import sin, cos, radians
from src.thread_draw_algo.draw_threads import count_xy

N = 600 # Вершин
R = 500 # Радиус окружности визуализации


def visualize(name):
    vertices = []
    edges = open(f"results/{name}.txt").read().strip().split("\n")

    plt.figure(figsize=(10, 10))
    plt.xlim(0, 1000), plt.ylim(-1000, 0)
    for e in edges:
        v1, v2 = e.split()
        x1, y1 = count_xy(N, R, int(v1))
        x2, y2 = count_xy(N, R, int(v2))
        plt.plot([y1, y2], [-x1, -x2], color="black", linewidth=0.2)
    plt.show()


if __name__ == '__main__':
    visualize("Поль Сезанн. Натюрморт с яблоками")