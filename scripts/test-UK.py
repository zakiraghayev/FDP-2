from pykrige.ok import OrdinaryKriging
import numpy as np
import matplotlib.pyplot as plt

#
data = np.array(
        [
            # X      Y      Z      fi
            [100.0, 200.0, 0.22],
            [200.0, 300.0, 0.23],
            [300.0, 400.0, 0.24],
            [400.0, 500.0, 0.23],
            [500.0, 600.0, 0.25],
            [600.0, 700.0, 0.28],
            [700.0, 800.0, 0.22],
            [800.0, 100.0, 0.26],
        ]
)

# data = np.array(
#     [
#         [0.0, 1.0, 0.47],
#         [1.0, 0.0, 0.56],
#         [1.0, 3.0, 0.74],
#         [3.0, 4.0, 1.47],
#         [4.0, 3.0, 1.74],
#     ]
# )

gridx = np.arange(100.0, 900.0, 10.0) #the number of grid on x axis
gridy = np.arange(200.0, 1000.0, 10.0) #the number of grid on y axis
print(data[:, 0])
OK = OrdinaryKriging(
    data[:, 0],
    data[:, 1],
    data[:, 2],
    variogram_model="linear",
    verbose=False,
    enable_plotting=True,
)

z, ss = OK.execute("grid", gridx, gridy)
plt.show()
