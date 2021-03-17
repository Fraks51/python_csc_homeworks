import matplotlib.pyplot as plt
from math import sin, cos, radians

N = 600 # Вершин
R = 500 # Радиус окружности визуализации

vertices = []
edges = open("results/Поль Сезанн. Натюрморт с яблоками.txt").read().strip().split("\n")

φ = 90
for i in range(N):
    x = cos(radians(φ)) * R
    y = sin(radians(φ)) * R
    vertices.append((x, y))
    φ -= 360 / N

x1, y1, x2, y2 = list(), list(), list(), list()

for e in edges:
    v1, v2 = e.split()
    ex_1, ey_1 = vertices[int(v1)-1]
    ex_2, ey_2 = vertices[int(v2)-1]
    x1.append(ex_1)
    x2.append(ex_2)
    y1.append(ey_1)
    y2.append(ey_2)
plt.figure(figsize=(10, 10))
plt.xlim(-500, 500), plt.ylim(-500, 500)
plt.plot(x1, y1, x2, y2, color="black", linewidth=0.2)
plt.show()

