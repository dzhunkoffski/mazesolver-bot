import numpy as np
from queue import Queue


class Graph():
    adj_list = None
    hasVisited = None
    distance = None
    prev = None

    bfs_q = Queue()
    width = None
    height = None

    maze = None

    def __init__(self, img):
        self.maze = np.full((img.size[0], img.size[1]), 0)
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if img.load()[i, j] == (0, 0, 0):
                    self.maze[i, j] = 1
                else:
                    self.maze[i, j] = 0

        w, h, = self.maze.shape
        self.width = w
        self.height = h
        self.distance = [[0 for _ in range(h)] for i in range(w)]
        self.hasVisited = [[False for _ in range(h)] for i in range(w)]
        self.prev = [[[] for _ in range(h)] for i in range(w)]

    def is_valid(self, curr_p, move):
        if 0 <= curr_p[0] + move[0] < self.width and 0 <= curr_p[1] + move[1] < self.height:
            return True if self.maze[curr_p[0] + move[0], curr_p[1] + move[1]] == 0 else False
        else:
            return False

    def bfs(self, start_point):
        movement = [
            [-1, 0],
            [1, 0],
            [0, 1],
            [0, -1]
        ]

        start_x, start_y = start_point
        self.bfs_q.put(start_point)
        self.hasVisited[start_x][start_y] = True

        while not self.bfs_q.empty():
            current_point = self.bfs_q.get()
            curr_x, curr_y = current_point[0], current_point[1]
            for move in movement:
                if self.is_valid(current_point, move):
                    neighbour_x = curr_x + move[0]
                    neighbour_y = curr_y + move[1]
                    if not self.hasVisited[neighbour_x][neighbour_y]:
                        self.hasVisited[neighbour_x][neighbour_y] = True
                        self.bfs_q.put([neighbour_x, neighbour_y])
                        self.distance[neighbour_x][neighbour_y] = self.distance[curr_x][curr_y] + 1
                        self.prev[neighbour_x][neighbour_y] = [curr_x, curr_y]

    def get_path(self, start_point, end_point):
        sx, sy = start_point
        ex, ey = end_point
        self.bfs(start_point)

        if start_point != end_point and self.distance[ex][ey] == 0:
            return None

        path = []
        curr_point = end_point
        while curr_point != start_point:
            cx, cy = curr_point[0], curr_point[1]
            path.append(curr_point)
            curr_point = self.prev[cx][cy]
        path.append(curr_point)
        return path


def solve_maze(image, start_point, end_point):
    graph = Graph(image)
    return graph.get_path(start_point, end_point)
