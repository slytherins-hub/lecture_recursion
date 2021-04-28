import os
import csv
import matplotlib.pyplot as plt

cwd_path = os.getcwd()
file_path = 'files'


def read_file(file_name):
    """
    Reads csv file from given folder
    :param file_name: (str) the name of csv file
    :return:
    """
    data_points = []
    with open(os.path.join(cwd_path, file_path, file_name), 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # skip header
        next(csv_reader)

        # read each row
        for row in csv_reader:
            data_points.append([float(number) for number in row])

    return data_points


def draw_data(data_points):
    """
    Function creates new figure and draw data points into scatter plot.
    :param data_points: (list of lists): each sublist is 1x2 list with x and y coordinate of a point.
    :return:
    """
    plt.scatter(
        [point[0] for point in data_points],
        [point[1] for point in data_points],
    )
    plt.show()


def main(file_name):
    # read data points
    data_points = read_file(file_name)

    # draw points
    draw_data(data_points)


if __name__ == '__main__':
    my_file = 'points.csv'
    main(my_file)
