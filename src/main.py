from PIL import Image
from skimage.filters import gaussian
import numpy as np
from src.thread_draw_algo.draw_threads import draw

dark_gradient = 0.36


def draw_from(filename):
    with Image.open(f'../data/{filename}.jpg') as im:
        width, height = im.size
        radius = min(width, height) / 2
        pixels = np.asarray(im) / 255
        # lets make white-black pic
        filtered_pixels = (pixels > dark_gradient).astype(pixels.dtype)
        result = draw(filtered_pixels, radius=radius)
        with open(f'../results/{filename}.txt', 'w') as f:
            for string in result:
                f.write(f"{string}\n")


if __name__ == '__main__':
    draw_from('Поль Сезанн. Натюрморт с яблоками')
