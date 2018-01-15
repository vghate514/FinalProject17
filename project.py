class Telescope():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def go_to(self,object):
        self.x += object[0]
        self.y += object[1]
        self.z += object[2]

    def position(self):
        print(self.x)
        print(self.y)
        print(self.z)

Tel_1 = Telescope()

sun = [23, 14, 30]

Tel_1.go_to(sun)
Tel_1.position()