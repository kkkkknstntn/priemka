import pygame as pg
from random import random
from collections import deque


def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


def check_next_node(x, y):
    if 0 <= x < cols and 0 <= y < rows and not grid[y][x]:
        return True
    else:
        return False


def get_next_nodes1(x, y):
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]


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

cols, rows = 20, 15
TILE = 40

pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])
clock = pg.time.Clock()
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

while True:
    # заполнить экран черным
    sc.fill(pg.Color('black'))
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
    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(100)
