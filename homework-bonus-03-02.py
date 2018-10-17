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
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0]
    ]

ways = [point(0, -1),
        point(-1, 0),
        point(1, 0),
        point(0, 1),
        point(-1, -1),
        point(1, -1),
        point(-1, 1),
        point(1, 1)]

steps = [point(1, 1, 2)]
map[1][1] = 'st'


# 廣度優先搜尋
def bfs(map, end):

    while(len(steps)):
        poi = steps[-1]
        if poi == end:
            map[poi.y][poi.x] = 'sp'
            print("found end!!!")
            for col in map:
                for row in col:
                    if str(row).isdigit():
                        if int(row) > 1:
                            print("{:2}".format(row-2), end="")
                        elif int(row) == 1:
                            print("{:>2}".format('*'), end="")
                        elif int(row) == 0:
                            print("{:2}".format(' '), end="")
                    else:
                        print("{:2}".format(row), end="")
                print()
            exit(0)
        for i in range(len(ways)):
            temp = poi + ways[i]
            temp.step = poi.step + 1
            # temp.step = 2
            if len(map[0]) > temp.x >= 0 and len(map) > temp.y >= 0 and map[temp.y][temp.x] == 0:
                steps.insert(0, temp)
                map[temp.y][temp.x] = temp.step

        steps.pop()

    print("can't found!!!")
    exit(0)


bfs(map, point(len(map[0])-1, len(map)-1))
