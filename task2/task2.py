# аргументы: "-file1 ./file1.txt -file2 ./file2.txt"

import math
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Task 2')
    parser.add_argument("-file1", required=True,  help="file1 var")
    parser.add_argument("-file2", required=True,  help="file1 var")

    args = parser.parse_args()

    file1_path = args.file1
    file2_path = args.file2

    with open(file1_path, 'r') as f1:
        file1 = f1.readlines()

    with open(file2_path, 'r') as f2:
        file2 = f2.readlines()

    x1_center = float(file1[0].split()[0])
    y1_center = float(file1[0].split()[1])

    r = float(file1[1])

    coordinates = [(float(xy[0]), float(xy[1])) for xy in [line.split() for line in file2]]

    for coordinate in coordinates:
        x = coordinate[0]
        y = coordinate[1]
        d = math.sqrt(math.pow((x - x1_center), 2) + math.pow((y - y1_center), 2))
        if d < r:
            print("точка внутри окружности")
        if d > r:
            print("точка снаружи")
        if d == r:
            print("точка лежит на окружности")
