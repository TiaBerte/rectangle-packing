from z3 import *
import matplotlib.pyplot as plt
import random
from matplotlib.patches import Rectangle


def read_data(instance):
    f = open(instance, 'r')
    data = f.read().split('\n')
    rect = []
    for i in range(0, len(data) - 1):
        rect.append(data[i].split())

    f.close()

    # Chip width
    W = int(rect[0][0])

    # Number of circuits
    n = int(rect[1][0])

    # Circuits sizes
    dimensions = [[int(rect[i][0]), int(rect[i][1])] for i in range(2, n + 2)]

    return W, n, dimensions


def max_z3(vars):
    max = vars[0]
    for v in vars[1:]:
        max = If(v > max, v, max)
    return max


def output(instance_path, model, order, W, H, n, w, h, x, y):

    if instance_path[-6: -4].isnumeric():
        number = instance_path[-6:-4]
    else:
        number = instance_path[-5:-4]

    out_name = 'out-' + number + '.txt'

    output_file = open(out_name, 'w')
    H = model.evaluate(H).as_string()
    output_file.writelines([str(W), ' ', str(H), '\n'])
    output_file.writelines([str(n), '\n'])

    for i in order:
        xi = model.evaluate(x[i]).as_string()
        yi = model.evaluate(y[i]).as_string()

        output_file.writelines([str(w[i]), ' ', str(h[i]), ' ', xi, ' ', yi, '\n'])

    output_file.close()
    return out_name, output_file


def output_rot(instance_path, model, order, W, H, n, w, h, x, y):

    if instance_path[-6: -4].isnumeric():
        number = instance_path[-6:-4]
    else:
        number = instance_path[-5:-4]

    out_name = 'out-' + number + '.txt'

    output_file = open(out_name, 'w')
    H = model.evaluate(H).as_string()
    output_file.writelines([str(W), ' ', str(H), '\n'])
    output_file.writelines([str(n), '\n'])

    for i in order:
        xi = model.evaluate(x[i]).as_string()
        yi = model.evaluate(y[i]).as_string()
        wi = model.evaluate(w[i]).as_string()
        hi = model.evaluate(h[i]).as_string()

        output_file.writelines([wi, ' ', hi, ' ', xi, ' ', yi, '\n'])

    output_file.close()

    return out_name, output_file


def display_sol(solution_path):
    random.seed(10)

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
        ax.add_patch(Rectangle((xi, yi), wi, hi, fill=1, alpha=1,
                               facecolor=(random.random(), random.random(), random.random())))

    if solution_path[-6: -4].isnumeric():
        number = solution_path[-6:-4]
    else:
        number = solution_path[-5:-4]
    plt.title('Solution of instance {}'.format(number))
    plt.show()


def read_data(instance):

    f = open(instance, 'r')
    data = f.read().split('\n')
    rect = []
    for i in range(0, len(data)-1):
        rect.append(data[i].split())

    f.close()

    # Chip width
    W = int(rect[0][0])

    # Number of circuits
    n = int(rect[1][0])

    # Circuits sizes
    dimensions = [[int(rect[i][0]), int(rect[i][1])] for i in range(2, n+2)]
    return W, n, dimensions
