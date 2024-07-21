# IAI_AAT_1BM22AI008


Name: Akash S.S

USN: 1BM22AI008

Section: 4A

Subject: IAI AAT HackerRank



## 1. Pacman-DFS

```python
pacman_x, pacman_y = map(int, input().split())
food_x, food_y = map(int, input().split())
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

stack = [(pacman_x, pacman_y, [])]
node_expanded = []
answer_routes = None

while stack:
    x, y, path = stack.pop()
    path = path + [(x, y)]

    node_expanded.append((x, y))

    if x == food_x and y == food_y:
        answer_routes = path
        break

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < n and 0 <= next_y < m and grid[next_x][next_y] in '-.':
            grid[next_x][next_y] = '='
            stack.append((next_x, next_y, path))

print(len(node_expanded))
for px, py in node_expanded:
    print(px, py)

if answer_routes:
    print(len(answer_routes) - 1)
    for px, py in answer_routes:
        print(px, py)





``` 

## 2.  Pacman-BFS

```python
from collections import deque

pacman_x, pacman_y = map(int, input().split())
food_x, food_y = map(int, input().split())
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

queue = deque([(pacman_x, pacman_y, [])])
node_expanded = []
answer_routes = None

while queue:
    x, y, path = queue.popleft()
    path = path + [(x, y)]

    node_expanded.append((x, y))

    if x == food_x and y == food_y:
        answer_routes = path
        break

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < n and 0 <= next_y < m and grid[next_x][next_y] in '-.':
            grid[next_x][next_y] = '='
            queue.append((next_x, next_y, path))

print(len(node_expanded))
for px, py in node_expanded:
    print(px, py)

if answer_routes:
    print(len(answer_routes) - 1)
    for px, py in answer_routes:
        print(px, py)



```


## 3. Tic Tac Toe

```python
#!/bin/python3

def nextMove(player, board):
    Empty = '_'
    opponent = 'O' if player == 'X' else 'X'

    def empty_board(b):
        return all(cell == Empty for row in b for cell in row)

    def check_and_print(r, c):
        print(f"{r} {c}")
        return True

    def search_board(marker, b):
        for i in range(3):
            if b[i].count(marker) == 2 and Empty in b[i]:
                return check_and_print(i, b[i].index(Empty))

            col = [b[j][i] for j in range(3)]
            if col.count(marker) == 2 and Empty in col:
                return check_and_print(col.index(Empty), i)

        diag1 = [b[i][i] for i in range(3)]
        diag2 = [b[i][2 - i] for i in range(3)]
        if diag1.count(marker) == 2 and Empty in diag1:
            idx = diag1.index(Empty)
            return check_and_print(idx, idx)
        if diag2.count(marker) == 2 and Empty in diag2:
            idx = diag2.index(Empty)
            return check_and_print(idx, 2 - idx)
        return False

    if search_board(player, board) or search_board(opponent, board):
        return

    if board[1][1] == Empty:
        print("1 1")
        return

    for (r, c) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if board[r][c] == Empty:
            print(f"{r} {c}")
            return

    for (r, c) in [(0, 1), (1, 0), (1, 2), (2, 1)]:
        if board[r][c] == Empty:
            print(f"{r} {c}")
            return

if __name__ == '__main__':
    player = input().strip()
    board = [input().strip() for _ in range(3)]
    nextMove(player, board)


```

