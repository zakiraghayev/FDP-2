# NOTE: This is a program that takes images, and gets black pixels corrdinates which are border dots in picture
# Then after it will make 3D module from x, y , z coordinates (z will be given)
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import csv


class ImageCordinater(object):
    """get picture and converts black pixels to x, y coordinates"""

    def __init__(self, image_url, z_coordinate):
        super(ImageCordinater, self).__init__()
        self.image_url = image_url
        self.z = z_coordinate

    def cross_coordinates(self, case=False):
        image = Image.open(self.image_url)
        pixels = image.load()
        width, height = image.size
        cross_coor = [[], []]
        # Start corrdinations
        for col in range(width):
            for row in range(height):
                if pixels[col, row] == (0, 0, 0):
                    if col < 389 or case:
                        cross_coor[0].append(col)
                        cross_coor[1].append(row)
        return cross_coor

    def coordinates(self):
        image = Image.open(self.image_url)
        pixels = image.load()
        width, height = image.size
        borders= [[], [], []] #X and Y coordinates
        CF = self.CF()
        # Start corrdinations
        for col in range(width):
            for row in range(height):
                if pixels[col, row] == (0, 0, 0):
                    borders[0].append(col*CF)
                    borders[1].append(row*CF)
                    borders[2].append(self.z)
                    # borders.append((col, row, self.z_coordinate))

        return borders

    def CF(self, image="X-Field-Layers/CF.jpg"):
        """ find converstion from pixel to km """
        CF_img = ImageCordinater(image, 0)
        row, col = CF_img.cross_coordinates()
        print(len(row))
        cf = (2*3280.84)/len(row) # 2km -> feet then one pixel with feet
        return cf

class _3DSystem(object):
    """docstring for 3DSystem."""

    def __init__(self):
        super(_3DSystem, self).__init__()
        # Create 3D coordinate system
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

    def ready_all_data(self, images_data):
        #                       X   y  z
        X_FIELD_COORDINATES = [[], [], []]
        for image_data in images_data:
            # image_data - > [image_url, z_coordinate]
            coordinates = ImageCordinater(image_data[0], image_data[1]).coordinates()
            # coordinates = [[x], [y], [z]]

            X_FIELD_COORDINATES[0].extend(coordinates[0])
            X_FIELD_COORDINATES[1].extend(coordinates[1])
            X_FIELD_COORDINATES[2].extend(coordinates[2])

        return X_FIELD_COORDINATES

    def plot_X_FIELD(self, XFC):
        # Creating color map
        surf = self.ax.plot_trisurf(XFC[0], XFC[1], XFC[2], alpha=0.5, cmap = plt.get_cmap('Dark2'), edgecolor ='none')
        self.fig.colorbar(surf, ax = self.ax, shrink = 0.5, aspect = 5)
        plt.show()

    def ready_all_data_from_csv(self, filename):
        with open(filename, newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            # x, y, z = [], [], []
            data = []
            for row in filereader:
                data.append(row)

            csvData = np.array(data)
            csvData = csvData.astype(np.float)
            x, y, z = csvData[:,0], csvData[:,1], csvData[:,2]

        return [ x, y, z ]



    def save(self, X_FIELD_DATA):
        with open('DATA-BASE/X_FIELD_DATA.csv', 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range( len(X_FIELD_DATA[0]) )  :
                filewriter.writerow([ X_FIELD_DATA[0][i], X_FIELD_DATA[1][i], -1*X_FIELD_DATA[2][i] ])

    def plot_test_data(self, arg):
        # self.ax.plot3D(arg[0], arg[1], arg[2], 'gray')
        self.ax.scatter3D(arg[0], arg[1], arg[2], c=arg[2], cmap='Greens');
        plt.show()


if __name__ == '__main__':
    # DATA PREPERATION
    init_depth = 9800 # from data it can be concluded that it inceaments 100 feet
    images_data = []
    for i in range(0, 14):
         images_data.append([f"X-Field-Layers/X-Field-{i+1}.jpg", init_depth + ( i*100 )])

    # # CONSTRUCTION
    system = _3DSystem()
    X_FIELD_DATA = system.ready_all_data_from_csv('DATA-BASE/X_FIELD_DATA.csv')
    system.plot_X_FIELD(X_FIELD_DATA)

    # DATA
    # system = _3DSystem()
    # X_FIELD_DATA = system.ready_all_data(images_data)
    # system.save(X_FIELD_DATA)
