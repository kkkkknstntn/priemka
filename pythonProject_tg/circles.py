import pygame as pg
from heapq import *
from random import random
from collections import deque


def get_circle(x, y):
    return (x * TILE + TILE // 2, y * TILE + TILE // 2), TILE // 4


def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2

def check_next_node(x, y):
    if 0 <= x < cols and 0 <= y < rows and not grid[y][x]:
        return True
    else:
        return False

def get_click_mouse_pos():
    x, y = pg.mouse.get_pos()
    grid_x, grid_y = x // TILE, y // TILE
    pg.draw.rect(sc, pg.Color('red'), get_rect(grid_x, grid_y))
    click = pg.mouse.get_pressed()
    if click[0]:
        return (grid_x, grid_y), 1
    elif click[2] :
        return (grid_x, grid_y), 2
    else:
        return False, 0
def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}
    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break
        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return queue, visited


def dfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}
    while queue:
        cur_node = queue.pop()
        if cur_node == goal:
            break
        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return queue, visited

def get_next_nodes1(x, y):
    check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [(grid[y + dy][x + dx], (x + dx, y + dy)) for dx, dy in ways if check_next_node(x + dx, y + dy)]
def get_next_nodes(x, y):
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]



cols, rows = 20, 15
TILE = 40

pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])
clock = pg.time.Clock()


grid = [[random() * 10 for col in range(cols)] for row in range(rows)]

# dict of adjacency lists
graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

# BFS settings
start = (0, 7)
goal = (22, 7)
queue = []
heappush(queue, (0, start))
cost_visited = {start: 0}
visited = {start: None}


# препятствия
grid = [[1 if random() < 0.2 else 0 for col in range(cols)] for row in range(rows)]
grid[0][0]=0
# список смежности
graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if not col:
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

# входные данные для BFS
start = (0, 0)
goal = start
queue = deque([start])
visited = {start: None}




def color(r):
    return 25 * r, 25 * r, 25 * r, 255
dks =1
b=0
while b<1:
    sc.fill(pg.Color('black'))
    a,b = get_click_mouse_pos()
    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(7)
if b==2:
    grid = [[random() * 10 for col in range(cols)] for row in range(rows)]

    # dict of adjacency lists
    graph = {}
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

    # BFS settings
    start = (0, 7)
    goal = (22, 7)
    queue = []
    heappush(queue, (0, start))
    cost_visited = {start: 0}
    visited = {start: None}

while True:
                sc.fill(pg.Color('black'))
                for i in pg.event.get():
                    if i.type == pg.QUIT:
                        exit()
                    elif i.type == pg.K_UP:
                        print(1)
                        if b==1:
                            # препятствия
                            grid = [[1 if random() < 0.2 else 0 for col in range(cols)] for row in range(rows)]
                            grid[0][0] = 0
                            # список смежности
                            graph = {}
                            for y, row in enumerate(grid):
                                for x, col in enumerate(row):
                                    if not col:
                                        graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

                            # входные данные для BFS
                            start = (0, 0)
                            goal = start
                            queue = deque([start])
                            visited = {start: None}
                        else:
                            print(1)
                            grid = [[random() * 10] for row in range(rows)]

                            # dict of adjacency lists
                            graph = {}
                            for y, row in enumerate(grid):
                                for x, col in enumerate(row):
                                    graph[(x, y)] = graph.get((x, y), []) + get_next_nodes1(x, y)

                            # BFS settings
                            start = (0, 7)
                            goal = (22, 7)
                            queue = []
                            heappush(queue, (0, start))
                            cost_visited = {start: 0}
                            visited = {start: None}


                if b == 2:
                    sc.fill(pg.Color('black'))
                    # fill screen

                    [[pg.draw.rect(sc, pg.Color(color(col)), get_rect(x, y), border_radius=TILE // 5)
                      for x, col in enumerate(row) if col] for y, row in enumerate(grid)]
                    # draw BFS work
                    [pg.draw.rect(sc, pg.Color('green'), get_rect(x, y), 2) for x, y in visited]
                    [pg.draw.rect(sc, pg.Color('blue'), get_rect(*xy), 2) for _, xy in queue]
                    pg.draw.circle(sc, pg.Color('yellow'), *get_circle(*goal))

                    if queue:
                        cur_cost, cur_node = heappop(queue)
                        if cur_node == goal:
                            queue = []
                            continue

                        next_nodes = graph[cur_node]
                        for next_node in next_nodes:
                            neigh_cost, neigh_node = next_node
                            new_cost = cost_visited[cur_node] + neigh_cost

                            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                                heappush(queue, (new_cost, neigh_node))
                                cost_visited[neigh_node] = new_cost
                                visited[neigh_node] = cur_node

                    # draw path
                    path_head, path_segment = cur_node, cur_node
                    while path_segment:
                        pg.draw.circle(sc, pg.Color('orange'), *get_circle(*path_segment))
                        path_segment = visited[path_segment]
                    pg.draw.circle(sc, pg.Color('red'), *get_circle(*start))
                    pg.draw.circle(sc, pg.Color('red'), *get_circle(*path_head))
                    [exit() for event in pg.event.get() if event.type == pg.QUIT]
                    pg.display.flip()
                    clock.tick(7)

                if b == 1:

                            # нарисовать препятсвия
                            [[pg.draw.rect(sc, pg.Color('white'), get_rect(x, y), border_radius=TILE // 5)
                              for x, col in enumerate(row) if col] for y, row in enumerate(grid)]
                            # рисование работы BFS
                            [pg.draw.rect(sc, pg.Color('cyan'), get_rect(x, y)) for x, y in visited]
                            [pg.draw.rect(sc, pg.Color('darkgrey'), get_rect(x, y)) for x, y in queue]

                            # bfs, получение пути до выбранной клетки
                            mouse_pos, flag = get_click_mouse_pos()
                            if flag == 1 and mouse_pos and not grid[mouse_pos[1]][mouse_pos[0]]:
                                queue, visited = bfs(start, mouse_pos, graph)
                                goal = mouse_pos
                            if flag == 2 and mouse_pos and not grid[mouse_pos[1]][mouse_pos[0]]:
                                queue, visited = dfs(start, mouse_pos, graph)
                                goal = mouse_pos

                            # рисование пути
                            path_head, path_segment = goal, goal
                            while path_segment and path_segment in visited:
                                pg.draw.rect(sc, pg.Color('yellow'), get_rect(*path_segment), TILE, border_radius=TILE // 3)
                                path_segment = visited[path_segment]
                            pg.draw.rect(sc, pg.Color('blue'), get_rect(*start), border_radius=TILE // 3)
                            pg.draw.rect(sc, pg.Color('magenta'), get_rect(*path_head), border_radius=TILE // 3)
                            # обязательные строки


                pg.display.flip()
                clock.tick(100)
