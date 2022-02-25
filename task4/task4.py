# аргументы: "-file ./file.txt"


import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Task 4')
    parser.add_argument('-file', required=True, type=str, help='file')
    args = parser.parse_args()

    file_path = args.file

    with open(file_path, 'r') as f:
        nums = [int(x) for x in f.readlines()]

    d = sorted(nums)[len(nums) // 2]
    print(sum(abs(v - d) for v in nums))

