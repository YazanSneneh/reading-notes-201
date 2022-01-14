
class Geometry:
    shapes = ['circle', 'rectange','square']
    def __init__(self, shape, height, width):
        self.shape = shape
        self.height = height
        self.width = width


    @classmethod
    def create_rectangle(cls, height, width):
        return cls(cls.shapes[1], height, width)

    @classmethod
    def create_square(cls, height, width):
        return cls(cls.shapes[2], height,width)

    @classmethod
    def create_circle(cls, height, width):
        return cls(cls.shapes[0], height, width)

    def calcArea(self):
        return (f"{self.shape} area is {self.height * self.width}")

    def get_name(self):
        return self.shape

    def __str__(self):
        return f"object {self.shape} from class Geometry, width ={self.width} and height ={self.height}"


rectangle = Geometry.create_rectangle(50.6, 20.2)
# print(rectangle.calcArea())
print(rectangle)