from PIL import Image
from skimage.filters import gaussian
import numpy as np
from src.thread_draw_algo.draw_threads import draw


def draw_from(filename):
    im = Image.open(f'../data/{filename}.jpg')
    width, height = im.size
    radius = min(width, height) / 2
    pixels = np.asarray(im) / 255
    filtered_pixels = np.array(list(map(lambda vec: np.array(list(map(lambda x: 1 if x > 0.36 else 0, vec))), pixels)))
    result = draw(filtered_pixels, radius=radius)
    f = open(f'../results/{filename}.txt', 'w')
    for i, j in result:
        f.write(f"{i} {j}\n")


def draw_square():
    square_pixels = np.array([np.array([1 for j in range(1001)]) for i in range(1001)])
    for i in range(450, 550):
        for j in range(450, 550):
            square_pixels[i][j] = 0
    result = draw(square_pixels, radius=500)
    f = open(f'../results/square.txt', 'w')
    for i, j in result:
        f.write(f"{i} {j}\n")


if __name__ == '__main__':
    draw_from('Поль Сезанн. Натюрморт с яблоками')