import os, sys, math, numpy, itertools, time

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))


def main():
    triangle = []
    with open("67.txt", "r") as f:
        for line in f:
            triangle.append([int(x) for x in line.split()])

    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # print(triangle[i + 1])
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    print(triangle[0][0])


if __name__ == "__main__":
    main()
