import matplotlib.pyplot as plt
import numpy as np
import csv
from kriging import OK
from ThreeDModule import ImageCordinater, _3DSystem

class Distribution(object):
    """docstring for Distribution."""

    def __init__(self, x, y, z , data):
        super(Distribution, self).__init__()
        self.x = np.array(x) #x coordinates of wells as array
        self.y = np.array(y) #y coordinates of wells as array
        self.z = z  # depth of the section analyzed
        self.data = np.array(data)

        # Griding on plot
        self.grid = np.zeros((200,200),dtype='float32') # float32 gives us a lot precision

    def show(self):
        # DO MAIN WORK
        grid = OK(self.x, self.y, self.data, (800,500), self.grid)
        plt.imshow(grid.T,origin='lower',interpolation='nearest',cmap='jet')
        plt.scatter(self.x, self.y, c=self.data, s=20)
        plt.grid()
        plt.show()

class Wells(object):
    """docstring for Wells."""

    def __init__(self, well_jpg, well_number):
        super(Wells, self).__init__()
        self.cf = 10.845752066115702 #calculated beforehand
        self.well_jpg = well_jpg
        self.well_number = well_number
        self.inital_coordinates()

    def inital_coordinates(self):
        well = ImageCordinater(self.well_jpg, self.well_number)
        coordinate = well.cross_coordinates(True)
        xmin, xmax = min(coordinate[0]), max(coordinate[0])
        ymin, ymax = min(coordinate[1]), max(coordinate[1])
        # self.cf = well.CF()

        x, y = (xmin+xmax)/2, (ymin+ymax)/2

        self.x, self.y = x*self.cf, y*self.cf
        return self.x, self.y

    def save(self, NW = 6):
        with open('../DATA-BASE/X_WELLS_DATA.csv', 'a+', newline='') as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow([ self.x, self.y, self.well_number ])

# TODO: add elevation horizontal well corrdinate

if __name__ == '__main__':
    wells_data = [ [], [], [], [0.23, 0.21, 0.19, 0.21, 0.25, 0.24] ]
    for i in range(2, 8):
        well = Wells(f"X-Wells/Wells-Extend-{i}.jpg", i-1)
        # well.save()
        wells_data[0].append(well.x)
        wells_data[1].append(well.y)
        wells_data[2].append(1)
    print(wells_data[0], wells_data[1], wells_data[2])
    dist = Distribution(wells_data[0], wells_data[1], wells_data[2], wells_data[3])
    dist.show()
