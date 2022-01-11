# solution_path must contain the path of the solutions.
# instance must contain the number of the instance whose
# solution plot is desired.

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random


instance = 28
solution_path = '*/out/out-' \
                + str(instance) + '.txt'
try:
    f = open(solution_path, 'r')

    data = f.read().split('\n')
    rect = []
    for i in range(0, len(data)):
        rect.append(data[i].split())
    f.close()

    if rect[0][0] == 'No':
        print('No solution has been found for this instance.')

    else:
        W = int(rect[0][0])
        H = int(rect[0][1])
        n = int(rect[1][0])

        fig, ax = plt.subplots()
        plt.xticks(range(1,W))
        plt.yticks(range(1,H))
        ax.grid()
        ax.set_xlim(xmin=0, xmax=W)
        ax.set_ylim(ymin=0, ymax=H)

        for i in range(2, n+2):
            xi = int(rect[i][2])
            yi = int(rect[i][3])
            wi = int(rect[i][0])
            hi = int(rect[i][1])

            ax.add_patch(Rectangle((xi, yi), wi, hi, fill=1, alpha=1, facecolor=(random.random(), random.random(), random.random())))
        digits = solution_path[4:]
        number = digits[:-3]
        plt.title('Solution of instance {}'.format(instance))
        plt.show()

except :
    solution_path = 'C:/Users/Mattia/Desktop/cdmo project/CP/out/out-' \
                    + str(instance) + '#.txt'

    f = open(solution_path, 'r')

    data = f.read().split('\n')
    rect = []
    for i in range(0, len(data)):
        rect.append(data[i].split())
    f.close()

    W = int(rect[0][0])
    H = int(rect[0][1])
    n = int(rect[1][0])

    fig, ax = plt.subplots()
    plt.xticks(range(1,W))
    plt.yticks(range(1,H))
    ax.grid()
    ax.set_xlim(xmin=0, xmax=W)
    ax.set_ylim(ymin=0, ymax=H)

    for i in range(2, n+2):
        xi = int(rect[i][2])
        yi = int(rect[i][3])
        wi = int(rect[i][0])
        hi = int(rect[i][1])
        ax.add_patch(Rectangle((xi, yi), wi, hi, fill=1, alpha=1, facecolor=(random.random(), random.random(), random.random())))
    digits = solution_path[4:]
    number = digits[:-4]

    print('The solution isn\'t the optimal one.')
    plt.title('Solution of instance {}'.format(instance))
    plt.show()

