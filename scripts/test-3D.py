from pykrige.ok3d import OrdinaryKriging3D
from pykrige.uk3d import UniversalKriging3D
import numpy as np
from matplotlib import pyplot as plt


data = np.array(
    [
        # X      Y      Z      fi
        [100.0, 200.0, 9800.0,  0.22],
        [200.0, 300.0, 10000.0, 0.23],
        [300.0, 400.0, 10100.0, 0.24],
        [400.0, 500.0, 10200.0, 0.23],
        [500.0, 600.0, 10300.0, 0.25],
        [600.0, 700.0, 10400.0, 0.28],
        [700.0, 800.0, 10500.0, 0.22],
        [800.0, 900.0, 10600.0, 0.26],
    ]
)

gridx = np.arange(90.0, 900.0, 50)
gridy = np.arange(90.0, 900.0, 50)
gridz = np.arange(9700.0, 106   50.0, 50)

ok3d = OrdinaryKriging3D(
    data[:, 0], data[:, 1], data[:, 2], data[:, 3], variogram_model="spherical"
)
k3d1, ss3d = ok3d.execute("grid", gridx, gridy, gridz)
fig = plt.figure()
# show the 3D rotated projection
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(k3d1[:,0], k3d1[:,1], k3d1[:,2], rstride=1, cstride=1, facecolors=plt.cm.BrBG(k3d1[:,3]), shade=False)
plt.show()
