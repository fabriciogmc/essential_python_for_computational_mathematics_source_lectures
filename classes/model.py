# A simple class to model a triangle.
class Triangle:
    def __init__(self, sides):
        """
        Sides is a list containing
        triangle's sides
        """
        self.sides = sides

    def perimeter(self):
        perimeter = 0
        for side in self.sides:
            perimeter += side
        return perimeter
