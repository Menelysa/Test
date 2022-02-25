# аргументы:  "-n 5 -m 4"


import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Task 1')
    parser.add_argument('-n', required=True, type=int, help='n variable')
    parser.add_argument('-m', required=True, type=int, help='m variable')

    args = parser.parse_args()

    n = args.n
    m = args.m

    massiv1 = m * [int(i) for i in range(1, n + 1)]
    massiv2 = ['']
    put = []
    count = 0
    while massiv2[-1] != 1:
        massiv2.clear()
        for j in range(count, m + count):
            massiv2.append(massiv1[j])
            count += 1
        massiv2_2 = massiv2.copy()
        put.append(massiv2_2)
        count -= 1
    for p in range(len(put)):
        print(put[p][0], end='')
