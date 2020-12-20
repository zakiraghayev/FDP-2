import copy
import numpy as np
from geostatistics.kriging import kriging
import matplotlib.pyplot as plt
from Distribution import Wells

class observation: pass
class estimation: pass

# wells_data = [ [], [], [], [0.244, 0.268, 0.315, 0.20, 0.195, 0.244] ] #saturation

# wells_data = [ [], [], [], [0.228, 0.281, 0.222, 0.241, 0.215 ,0.211] ] #Porostiy
wells_data = [ [], [], [], [395, 247, 2163, 769, 719, 996] ] #permeability
for i in range(1, 7):
    well = Wells(f"X-Wells/Wells-Extend-{i}.jpg", i)
    # well.save()
    wells_data[0].append(int(well.x))
    wells_data[1].append(int(well.y))
    wells_data[2].append(1)

observation.X = np.array(wells_data[1])
observation.Y = np.array(wells_data[0])
observation.Z = np.array([1,1,1,1,1,1])

observation.F = np.array(wells_data[3])
#
# plt.figure()
# plt.scatter(observation.X, observation.Y, s=20  , c=observation.F, alpha=0.5)
# plt.colorbar()
#
# plt.xlabel("X")
# plt.ylabel("Y")

observation.type = 'exponential'
observation.nugget = 0
observation.sill = 1000
observation.range = 14000

N = 1200
xlin = np.linspace(0, 35000, N)
ylin = np.linspace(0, 35000, N)

[Xmesh, Ymesh] = np.meshgrid(xlin, ylin)


estimation.X = Xmesh.flatten()
estimation.Y = Ymesh.flatten()
estimation.Z = np.ones_like(estimation.X)

krig = kriging(observation)
krig.ordinary(estimation)
plt.figure()

ctrf = plt.contourf(Xmesh, Ymesh, estimation.F.reshape(N, N))
plt.colorbar()
plt.title("Porostiy")
plt.xlabel('X, feet')
plt.ylabel('Y, feet')
plt.show()
