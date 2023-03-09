import numpy as np
from sympy import solve
from sympy.abc import x as par1
from sympy.abc import y as par2


lim = 100
rs = 5
re = 50
c = 0


def dist(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    dist = np.linalg.norm(point1 - point2)
    return dist


def randdot(rows, cols):
    newNode = [np.random.randint(0, rows), np.random.randint(0, cols)]
    return newNode

def equations(x,y,x2,y2) -> int:
    start = [x2,y2]
    k = (y - y2) / (x - x2)
    b = y2 - k * x2
    solves=solve([par2-k*par1-b, (par1-x)**2+(par2-y)**2-rs**2],[par1,par2])
    lens=[]
    for i in solves:
        lens.append(dist(start,[float(i[0]),float(i[1])]))
    idx = lens.index(min(lens))
    [x2, y2] = int(solves[idx][0]), int(solves[idx][1])
    print(int(solves[idx][0]), int(solves[idx][1]))
    return x2, y2


def rrt(start, end,rows,cols):
    randNode = randdot(rows,cols)
    start = np.array(start)
    x,y =start[0],start[1]
    end = np.array(end)
    lenedge = dist(start, randNode)
    print(lenedge, rs, randNode)
    x2,y2 = randNode[0],randNode[1]
    newNode = np.array(equations(x,y,x2,y2))
    print(newNode)
    return lenedge, rs, newNode

# elif event.key == pygame.K_TAB:
# lenedge, rs, node = RRT.rrt([x, y], [x1, y1], rows, cols)
# x2, y2 = node[0], node[1]
# grid[node[0]][node[1]] = PURPLE
# # solves, lens, idx =  RRT.equations(x,y,x2,y2)
# # print(int(solves[idx][0]))
# # grid[int(solves[idx][0])][int(solves[idx][1])] = ORANGE