from QiPan import QiPan
import numpy as np

arr = np.array([[2,3],
                [2,4],
                [2,5],
                [2,6],
                [3,2],
                [3,4],
                [3,6],
                [4,2],
                [4,3],
                [4,4],
                [4,5],
                [4,6]])
qipan = QiPan(arr)
qipan.draw_potential_3d()
qipan.draw_potential_2d()
