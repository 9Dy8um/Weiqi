import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


class QiPan:

    def __init__(self, arr: np.ndarray):
        self.arr = arr
        self.shi = self.__set_shi_sum(arr)

    def draw_potential_3d(self):
        Z = self.shi
        fig: plt.Figure = plt.figure()
        ax = fig.add_subplot(projection='3d')
        x = np.arange(0, 19, 1)
        y = np.arange(0, 19, 1)
        X, Y = np.meshgrid(x, y)
        ax.plot_surface(X, Y, Z, cmap=cm.rainbow)
        ax.set_xlim(0, 18)
        ax.set_xticks(np.arange(0, 18))
        ax.set_ylim(0, 18)
        ax.set_yticks(np.arange(0, 18))
        plt.show()

    def draw_potential_2d(self):
        Z = self.shi
        fig: plt.Figure = plt.figure()
        ax = fig.add_subplot()
        ax.imshow(Z)
        ax.set_xlim(-0.5, 18.5)
        ax.set_ylim(-0.5, 18.5)
        ax.set_xticks(np.arange(0, 18+1))
        ax.set_yticks(np.arange(0, 18+1))
        plt.grid()
        plt.show()

    def __get_shi_single(self, mu_1: int, mu_2: int, sigma_1: int = 2, sigma_2: int = 2) -> np.ndarray:
        x = np.arange(0, 19, 1)
        y = np.arange(0, 19, 1)
        X, Y = np.meshgrid(x, y)
        Z = 1 * np.exp(-1 * 1 * ((-mu_2 + Y) ** 2 / (sigma_2 ** 2) +
                                 (-mu_1 + X) ** 2 / (sigma_1 ** 2)) / 2) / (2 * np.pi * sigma_1 * sigma_2)
        return Z

    def __set_shi_sum(self, arr: np.ndarray) -> np.ndarray:  # arr:点集
        shi: np.ndarray = np.zeros(shape=(19, 19))
        for i in arr:
            shi = shi + self.__get_shi_single(i[0], i[1])
        return shi
