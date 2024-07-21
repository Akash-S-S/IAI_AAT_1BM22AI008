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
