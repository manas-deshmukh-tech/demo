class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Vector:", self.x, self.y)


v = Vector(3, 4)
v.show()