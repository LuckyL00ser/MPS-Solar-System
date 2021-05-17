import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from itertools import count
from matplotlib.animation import FuncAnimation

radius_list = [6.96340000E8, 2439.7, 6051.8, 6371, 3389.5, 69911, 58232, 25362, 25622]
maxDim = 3.0E12

read_data = pd.read_csv("results.csv", header=0)
del read_data["Venus_X"]
del read_data["Venus_Y"]
del read_data["Venus_Z"]
planet_names = [name.split("_")[0] for name in read_data.columns[:-1:3]]

planet_records = read_data.to_numpy()
planet_records = planet_records[:, :-1]

planets = np.zeros((planet_records.shape[1] // 3, planet_records.shape[0], 3))
for index in range(0, planet_records.shape[1] // 3):
    planets[index] = planet_records[:, index * 3:index * 3 + 3]

fig = plt.figure()
plt.figure(figsize=(12, 12), dpi=80)
ax = plt.axes(projection='3d')
plt.title("Dead In Space")
plt.xlim([-maxDim, maxDim])
plt.ylim([-maxDim, maxDim])
ax.set_zlim(-maxDim, maxDim)

time_counter = count()


def animation(i):
    time_step = next(time_counter)*10
    plt.cla()
    for index in range(planets.shape[0]):
        r = max(radius_list[index], maxDim / 50)
        u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
        x = np.cos(u) * np.sin(v)
        y = np.sin(u) * np.sin(v)
        z = np.cos(v)

        # shift and scale sphere
        x = r * x + planets[index, time_step, 0]
        y = r * y + planets[index, time_step, 0]
        z = r * z + planets[index, time_step, 0]

        ax.plot_surface(x, y, z, alpha=0.5)
        ax.plot(planets[index, :time_step, 0], planets[index, :time_step, 1], planets[index, :time_step, 2], color="gray")
        ax.text(planets[index, time_step, 0], planets[index, time_step, 0], planets[index, time_step, 0], planet_names[index])


animation = FuncAnimation(plt.gcf(), animation, interval=1)
plt.tight_layout()
plt.show()
