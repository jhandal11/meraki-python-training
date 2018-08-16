class Point:
    def reset(self):
        self.x = 0
        self.y = 0

if __name__ == "__main__":

    p1 = Point()
    p2 = Point()

    p1.x = 5
    p1.y = 4

    p2.x = 3
    p2.y = 6
    print(p1.x, p1.y)
    print(p2.x, p2.y)

    p1.reset()
    p2.reset()

    print(p1.x, p1.y)
    print(p2.x, p2.y)
