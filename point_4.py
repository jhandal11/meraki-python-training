class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

if __name__ == "__main__":
    # Constructing a Point
    point1 = Point(3, 5)
    print(point1.x, point1.y)

    point2 = Point(3)
