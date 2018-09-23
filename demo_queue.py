class point:

    def __init__(self, x, y, s=0):
        self.x = x
        self.y = y
        self.step = s

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


map = [
    [0, 0, 0, 0, -1, 0],
    [-1, 0, -1, -1, -1, 0],
    [0, 0, 0, 0, 0, 0],
    [-1, 0, 0, -1, -1, 0],
    [0, 0, -1, -1, 0, 0],
    [0, 0, -1, 0, 0, 0],
    [-1, 0, -1, 0, -1, 0],
    [-1, 0, -1, -1, -1, -1],
    [0, 0, 0, 0, 0, 0],
    ]

ways = [point(0, -1), point(-1, 0), point(1, 0), point(0, 1)]

steps = [point(5, 8, 1)]
map[8][5] = 'st'


# 廣度優先搜尋
def bfs(map, end):

    while(len(steps)):
        poi = steps[-1]
        if poi == end:
            map[poi.y][poi.x] = 'sp'
            print("found end!!!")
            for col in map:
                outputline = ""
                for row in col:
                   outputline += "{:2}, ".format(row)
                print(outputline)
            exit(0)
        for i in range(4):
            temp = poi + ways[i]
            temp.step = poi.step + 1
            if temp.x >= 0 and temp.y >= 0 and temp.x < len(map[0]) and temp.y < len(map) and map[temp.y][temp.x] == 0:
                steps.insert(0, temp)
                map[temp.y][temp.x] = temp.step

        steps.pop()

    print("can't found!!!")
    exit(0)


bfs(map, point(5, 0))
