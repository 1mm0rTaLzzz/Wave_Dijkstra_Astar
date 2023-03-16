import numpy as np
from sympy import solve
from sympy.abc import x as par1
from sympy.abc import y as par2

rs = 20
re = 20
PURPLE = (139, 0, 250)
'''

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            # if dist()
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)

            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
            print(self.data)
        if self.right:
            self.right.PrintTree()
            print(self.data)

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

'''
#root = Node()
#root.PrintTree()


def dist(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    dist = np.linalg.norm(point1 - point2)
    return dist


def randdot(rows, cols):
    randNode = np.array([np.random.randint(0, rows), np.random.randint(0, cols)])
    return randNode


def equations(x, y, x2, y2) -> int:
    start = [x2, y2]
    try:
        k = (y - y2) / (x - x2)
        b = y2 - k * x2
        solves = solve([par2 - k * par1 - b, (par1 - x) ** 2 + (par2 - y) ** 2 - rs ** 2], [par1, par2])
        lens = []
        for i in solves:
            lens.append(dist(start, [float(i[0]), float(i[1])]))
        idx = lens.index(min(lens))
        [x2, y2] = int(solves[idx][0]), int(solves[idx][1])
    except:
        pass
    # print(int(solves[idx][0]), int(solves[idx][1]))
    return x2, y2


def rrt(start, rows, cols, tree):
    randNode = randdot(rows, cols)
    x, y = start[0], start[1]
    len_edge = dist(start, randNode)
    x2, y2 = randNode[0], randNode[1]
    if len_edge > rs:# or len_edge <= rs:
        newNode = np.array(equations(x, y, x2, y2))
        if newNode not in tree:
            tree = np.append(tree, newNode)
    else:
        newNode = randNode
        tree = np.append(tree, newNode)
    tree = tree.reshape(-1, 2).astype(np.int16)
    #start = newNode
    for j in range(len(tree)):
        near_node = nearest_node(newNode, tree, j)
    start = near_node
    print('gfh',start, newNode)
    return len_edge, rs, newNode, tree, start


def nearest_node(node, tree, num):
    temp_dist = []
    min_ind = -1
    min_dist = -1
    for i in range(0, num):
        mlen = dist(node, tree[i])
        #if min_dist == -1 or mlen < min_dist:
            #min_ind = i
            #min_dist = mlen
        if mlen != 0:
            temp_dist.append(mlen)
    if len(temp_dist)<2:
        temp_dist.append(1000)
    near_node = tree[temp_dist.index(min(temp_dist))]
    return near_node#tree[min_ind]
