class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


map = [
    [0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    ]

ways = [point(0, -1), point(-1, 0), point(1, 0), point(0, 1)]

steps = []


def dfs(map, poi, end):

    if poi.x < 0 or poi.y < 0 or poi.x >= len(map[0]) or poi.y >= len(map) or map[poi.y][poi.x] != 0:
        return

    steps.append(point(poi.x, poi.y))
    map[poi.y][poi.x] = 2
    if poi == end:
        print("found end!!!")
        for item in steps:
            print(item)
        for col in map:
            print(col)
        exit(0)
    else:
        for i in range(4):
            dfs(map, poi+ways[i], end)

        if len(steps) == 1:
            print("can't found!!!")
            exit(0)

        steps.pop()
        map[poi.y][poi.x] = 0


dfs(map, point(5, 8), point(5, 0))


